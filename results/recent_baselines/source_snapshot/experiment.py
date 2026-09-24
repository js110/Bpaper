"""Reproducible event simulation. Evaluation truth is never passed to the attack."""
import argparse,csv,gzip,hashlib,json,platform,time
from pathlib import Path
import numpy as np
from functools import lru_cache
from .model import Task,Observation,PublicBelief,predict,gates,choose_probe,posterior_metrics

@lru_cache(maxsize=64)
def load_channel(path):
    return np.load(path)['channel']

def candidates(side):
    rects=set()
    for width in sorted(set([1,2,max(2,side//2),max(2,3*side//4),side])):
        for x in range(0,side-width+1,max(1,width//2)):
            for y in range(0,side-width+1,max(1,width//2)):
                rects.add((x,x+width,y,y+width))
    for axis in range(2):
        for k in range(1,side):
            rects.add((0,k,0,side) if axis==0 else (0,side,0,k))
            rects.add((k,side,0,side) if axis==0 else (0,side,k,side))
    rects=sorted(rects)
    masks=np.array([Task('',0,0,r).mask(side) for r in rects],float)
    return rects,masks

def path_for(seed,user,side,slots,scenario,move):
    rng=np.random.default_rng(np.random.SeedSequence([seed,user,101]))
    if scenario=='commute':
        y=int(rng.integers(side));offset=int(rng.integers(2*(side-1)))
        v=(np.arange(slots)+offset)%(2*(side-1))
        return (np.minimum(v,2*(side-1)-v)*side+y).astype(int)
    state=int(rng.integers(side*side));out=[]
    for t in range(slots):
        out.append(state)
        if scenario!='static' and rng.random()<move:
            x,y=divmod(state,side);axis=int(rng.integers(4))
            dx,dy=[(1,0),(-1,0),(0,1),(0,-1)][axis]
            state=int(np.clip(x+dx,0,side-1)*side+np.clip(y+dy,0,side-1))
    return np.array(out)

def simulate(condition,seed,user,path,rects,masks,slots,side,log):
    delivery=condition['delivery'];willing=condition['willing'];on_time=condition['on_time']
    alpha_true=delivery*willing*on_time
    alpha_model=condition.get('alpha_model',alpha_true)
    move_model=condition['move_model']
    method=condition['method'];param=condition['param'];attack=condition['attack']
    channel=load_channel(condition['channel_file']) if method=='privic' else None
    # This public map contains a gate probability for EVERY possible location.
    # The attacker never receives the probability indexed by the true location.
    privic_qs=masks@channel.T if channel is not None else None
    rng=np.random.default_rng(np.random.SeedSequence([seed,int(user),202]))
    normal_ids=rng.integers(len(rects),size=slots)
    random_probe_ids=rng.integers(len(rects),size=slots)
    ext=rng.random((slots,4))
    legitimate_schedule=rng.random(slots)<condition.get('legitimate_fraction',.75)
    belief=PublicBelief(side,move_model,alpha_model)
    attacker=PublicBelief(side,condition.get('attacker_move',move_model),condition.get('attacker_alpha',alpha_model))
    prior=np.full(side*side,1/(side*side))
    sums={k:0. for k in ['hit','error_cells','peak','logloss','covered95','credible95','entropy']}
    prior_hit=0.;legit=0;opportunities=0;complete=0;reports=0;cap_violations=0;op_cells=set();done_cells=set()
    gate_times=[];rows=[];bin_counts=np.zeros(10);bin_hits=np.zeros(10);bin_peaks=np.zeros(10);error_m=0.
    for t in range(slots):
        # Identity resetting is an ideal control: discard past target-specific evidence.
        if condition.get('reset_every',0) and t%condition['reset_every']==0:
            belief.b=prior.copy()
            attacker.b=prior.copy()
        if t:
            belief.b=predict(belief.b,side,move_model)
            attacker.b=predict(attacker.b,side,attacker.move)
            prior=predict(prior,side,move_model)
        is_legit=bool(legitimate_schedule[t])
        if is_legit: idx=int(normal_ids[t])
        elif attack=='adaptive':
            from .model import binary_entropy
            qs=privic_qs if channel is not None else gates(belief.b,masks,alpha_model,method,param,t,rects)[:,None]
            likelihood=masks*(attacker.alpha*qs)
            information=binary_entropy((likelihood*attacker.b).sum(axis=1))-(binary_entropy(likelihood)*attacker.b).sum(axis=1)
            idx=int(np.argmax(information))
        else:idx=int(random_probe_ids[t])
        task=Task(f'{t}',t,t,rects[idx],is_legit)
        start=time.perf_counter_ns()
        q=channel@masks[idx] if channel is not None else float(gates(belief.b,masks[idx],alpha_model,method,param,t,[rects[idx]])[0])
        gate_times.append((time.perf_counter_ns()-start)/1000)
        bprior=belief.b.copy();mask=masks[idx].astype(bool);truth=int(path[t])
        eligible=bool(mask[truth])
        available=bool(ext[t,0]<delivery and ext[t,1]<willing and ext[t,2]<on_time)
        q_at_state=float(q[truth]) if channel is not None else q
        reported=bool(eligible and available and ext[t,3]<q_at_state)
        observation=Observation(task.task_id,t,reported)
        belief.observe(task,observation,q)
        attacker.observe(task,observation,q)
        if np.max(belief.b)>max(param,np.max(bprior))+1e-9 and method=='bsp':cap_violations+=1
        metrics=posterior_metrics(attacker.b,truth,side)
        for k,v in metrics.items():sums[k]+=v
        bn=min(9,int(metrics['peak']*10));bin_counts[bn]+=1;bin_hits[bn]+=metrics['hit'];bin_peaks[bn]+=metrics['peak']
        if condition['scenario']=='geolife':
            ties=np.flatnonzero(np.isclose(attacker.b,attacker.b.max(),rtol=1e-10,atol=1e-14))
            xy=np.array(np.unravel_index(ties,(side,side))).T-np.array(divmod(truth,side))
            error_m+=float(np.linalg.norm(xy*np.array([.3*111320/side,.4*111320*np.cos(np.deg2rad(39.95))/side]),axis=1).mean())
        else:error_m+=metrics['error_cells']*1000
        prior_hit+=posterior_metrics(prior,truth,side)['hit']
        if is_legit:
            legit+=1
            if eligible and available:opportunities+=1;op_cells.add(truth)
            if reported:complete+=1;done_cells.add(truth)
        reports+=reported
        if log:
            rows.append(dict(slot=t,task_id=task.task_id,rectangle=rects[idx],legitimate=is_legit,
                             reported=reported,q=q.tolist() if channel is not None else q,alpha_model=alpha_model,prior_peak=float(bprior.max()),
                             belief=attacker.b.tolist(),client_peak=float(belief.b.max()),evaluator_truth=truth,eligible=eligible,available=available,**metrics))
    out={k:v/slots for k,v in sums.items()}
    out.update(ece=float(np.abs(bin_hits-bin_peaks).sum()/slots),error_m=error_m/slots,seed=seed,user=str(user),scenario=condition['scenario'],condition=condition['id'],
               method=method,param=param,attack=attack,side=side,prior_hit=prior_hit/slots,
               legitimate=legit,opportunities=opportunities,complete=complete,reports=reports,
               utility=complete/opportunities if opportunities else float('nan'),
               raw_completion=complete/legit,coverage=len(done_cells)/len(op_cells) if op_cells else float('nan'),
               reward=complete,latency_slots=1.0 if reports else float('nan'),
               gate_us_p50=float(np.median(gate_times)),gate_us_p95=float(np.quantile(gate_times,.95)),
               cap_violations=cap_violations,alpha_true=alpha_true,alpha_model=alpha_model,move_model=move_model)
    return out,rows

def run(config_path):
    cfg=json.loads(Path(config_path).read_text());out=Path(cfg['output'])
    if out.exists() and (out/'rows.csv').exists():raise FileExistsError('immutable run already exists: '+str(out))
    out.mkdir(parents=True,exist_ok=True)
    (out/'config.json').write_text(json.dumps(cfg,indent=2))
    (out/'environment.json').write_text(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,platform=platform.platform(),
        code_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('src').glob('*.py')}),indent=2))
    allrows=[];failures=[];start=time.perf_counter();cache={}
    for ci,cond in enumerate(cfg['conditions']):
        side=cond.get('side',cfg['side']);slots=cfg['slots']
        if side not in cache:cache[side]=candidates(side)
        rects,masks=cache[side]
        if cond['scenario']=='geolife':
            data=np.load(cfg['geolife_file'])
            participants=[(int(data['users'][j]),int(data['users'][j]),data['paths'][j][:slots]) for j in range(len(data['users']))]
        else:
            participants=[(seed,u,path_for(seed,u,side,slots,cond['scenario'],cond['move_true'])) for seed in cfg['seeds'] for u in range(cfg['users_per_seed'])]
        with gzip.open(out/(cond['id']+'.jsonl.gz'),'wt') as f:
            for j,(seed,user,path) in enumerate(participants):
                try:
                    row,events=simulate(cond,seed,user,path,rects,masks,slots,side,True)
                    allrows.append(row)
                    f.write(json.dumps(dict(seed=seed,user=str(user),events=events))+'\n')
                except Exception as e:
                    failures.append(dict(condition=cond['id'],seed=seed,user=user,error=repr(e)))
                    (out/'failures.json').write_text(json.dumps(failures,indent=2))
                    raise
        print(f'{ci+1}/{len(cfg["conditions"])} {cond["id"]}: n={len(participants)} elapsed={time.perf_counter()-start:.1f}s',flush=True)
    with (out/'rows.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(allrows[0]));w.writeheader();w.writerows(allrows)
    (out/'failures.json').write_text(json.dumps(failures,indent=2))
    (out/'duration.json').write_text(json.dumps({'wall_seconds':time.perf_counter()-start}))
    return allrows

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--config',required=True);args=ap.parse_args();run(args.config)
