"""Construct a finite R-BSP ambiguity set from development/validation mobility data.

GeoLife contains trajectories but no real task-delivery/willingness/deadline logs.
Therefore mobility and prior uncertainty are data-derived here, while alpha is an
explicit externally supplied protocol parameter.
"""
import argparse,json
from pathlib import Path
import numpy as np


def state_exposure(states,side):
    states=np.asarray(states,dtype=int)
    x=states//side;y=states%side
    degree=4-(x==0).astype(int)-(x==side-1).astype(int)-(y==0).astype(int)-(y==side-1).astype(int)
    return degree/4.0


def fit_move_coarsened(paths,side=8):
    """MLE for P(cell changes | state)=v*deg(state)/4.

    Destination direction/distance is deliberately discarded. This matches the
    paper's reflecting-walk approximation while avoiding zero likelihood for
    observed multi-cell jumps.
    """
    paths=np.asarray(paths,dtype=int)
    src=paths[:,:-1].ravel();changed=(paths[:,1:]!=paths[:,:-1]).ravel().astype(float)
    exposure=state_exposure(src,side)
    nchange=float(changed.sum())
    if nchange==0:return 0.0
    stay=changed==0
    def deriv(v):
        return nchange/max(v,1e-15)-float(np.sum(exposure[stay]/np.maximum(1-v*exposure[stay],1e-15)))
    hi=1-1e-12
    if deriv(hi)>=0:return 1.0
    lo=1e-12
    for _ in range(80):
        mid=(lo+hi)/2
        if deriv(mid)>0:lo=mid
        else:hi=mid
    return float((lo+hi)/2)


def user_bootstrap(paths,side,reps,seed):
    rng=np.random.default_rng(seed);paths=np.asarray(paths)
    out=np.empty(reps,float)
    for r in range(reps):
        idx=rng.integers(len(paths),size=len(paths))
        out[r]=fit_move_coarsened(paths[idx],side)
    return out


def smoothed_prior(paths,side,pseudocount=.5):
    counts=np.bincount(np.asarray(paths,dtype=int).ravel(),minlength=side*side).astype(float)
    counts+=float(pseudocount)
    return (counts/counts.sum()).tolist()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--development',default='data/geolife_development.npz')
    ap.add_argument('--validation',default='data/geolife_validation.npz')
    ap.add_argument('--output',default='results/data_driven_ambiguity/models.json')
    ap.add_argument('--side',type=int,default=8)
    ap.add_argument('--alpha',type=float,default=.648)
    ap.add_argument('--bootstrap',type=int,default=2000)
    ap.add_argument('--confidence',type=float,default=.95)
    ap.add_argument('--seed',type=int,default=270926)
    a=ap.parse_args()
    if not (0<a.alpha<=1):raise ValueError('alpha must lie in (0,1]')
    dev=np.load(a.development);val=np.load(a.validation)
    dp=np.asarray(dev['paths']);vp=np.asarray(val['paths'])
    dev_hat=fit_move_coarsened(dp,a.side);val_hat=fit_move_coarsened(vp,a.side)
    pooled_hat=fit_move_coarsened(np.concatenate([dp,vp]),a.side)
    db=user_bootstrap(dp,a.side,a.bootstrap,a.seed)
    vb=user_bootstrap(vp,a.side,a.bootstrap,a.seed+1)
    tail=(1-a.confidence)/2
    dci=np.quantile(db,[tail,1-tail]);vci=np.quantile(vb,[tail,1-tail])
    lo=float(min(dci[0],vci[0]));hi=float(max(dci[1],vci[1]))
    moves=[]
    for x in [lo,pooled_hat,hi]:
        if not any(abs(x-y)<1e-10 for y in moves):moves.append(float(x))
    pooled=np.concatenate([dp,vp])
    pop_prior=smoothed_prior(pooled,a.side,.5)
    uniform=(np.ones(a.side*a.side)/(a.side*a.side)).tolist()
    models=[]
    for move in moves:
        models.append(dict(move=move,alpha=a.alpha,prior=uniform,prior_type='uniform'))
        models.append(dict(move=move,alpha=a.alpha,prior=pop_prior,prior_type='population_smoothed'))
    out=dict(
        schema='data-driven-rbsp-v1',
        construction='union of development and validation user-bootstrap mobility intervals; pooled center; uniform and smoothed population priors',
        side=a.side,alpha=a.alpha,
        alpha_provenance='externally specified protocol parameter; GeoLife has trajectories but no real task availability logs',
        fit_model='coarsened reflecting-walk change likelihood P(change|state)=v*degree(state)/4; destination direction and jump distance ignored',
        development=dict(users=int(len(dp)),estimate=dev_hat,ci=dci.tolist()),
        validation=dict(users=int(len(vp)),estimate=val_hat,ci=vci.tolist()),
        pooled=dict(users=int(len(pooled)),estimate=pooled_hat),
        confidence=a.confidence,bootstrap_replicates=a.bootstrap,bootstrap_seed=a.seed,
        move_interval=[lo,hi],move_candidates=moves,
        priors=['uniform','population_smoothed'],prior_pseudocount=.5,
        population_prior=pop_prior,models=models,
        test_data_used=False)
    p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['development','validation','pooled','move_interval','move_candidates']},indent=2))


if __name__=='__main__':main()
