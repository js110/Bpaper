import json,gzip,csv,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path.cwd()))
from src.model import gates,update,predict
from src.recent_baselines import pml_gates,pml_lp
from src.analyze_recent import lower_hull
out={}
rng=np.random.default_rng(170926);fails=[];pmlerr=[]
for t in range(300):
 n=16;b=rng.dirichlet(np.ones(n));mask=rng.random(n)<.5;alpha=float(rng.random());rho=float(rng.uniform(1/n,1))
 q=float(gates(b,mask,alpha,'bsp',rho,0)[0]);cap=max(rho,max(b));m=alpha*sum(b[mask])
 for y,prob in [(True,q*m),(False,1-q*m)]:
  if prob>1e-10 and max(update(b,mask,alpha,q,y))>cap+1e-9:fails.append(t)
 if q<1-1e-6:
  qq=min(1,q+1e-5);feasible=all(max(update(b,mask,alpha,qq,y))<=cap+1e-9 for y,prob in [(True,qq*m),(False,1-qq*m)] if prob>1e-12)
  if feasible:fails.append(('max',t))
 if t<100:
  eps=float(rng.uniform(.01,4));pq=pml_gates(b,mask,alpha,eps)[0];pmlerr.append(abs(pq*m-pml_lp(b,mask,alpha,eps)))
out['random_formula_checks']={'bsp_cases':300,'failures':fails,'pml_lp_cases':100,'pml_max_abs_objective_error':max(pmlerr)}
b=np.array([.2,.2,.2,.4]);mask=np.array([1,1,1,0]);out['silence_example']={'q':float(gates(b,mask,.9,'bsp',.4,0)[0]),'success_only_silence_peak':float(max(update(b,mask,.9,1,False)))}
geo={}
for split in ['development','validation','test']:
 a=np.load(f'data/geolife_{split}.npz');p=a['paths'];geo[split]={'n_users':len(p),'static_windows':int(sum(np.all(p==p[:,0,None],axis=1))),'cell_changes':int(np.sum(np.diff(p)!=0)),'total_adjacent_pairs':int(p.shape[0]*(p.shape[1]-1)),'unique_cells_median':float(np.median([len(set(row)) for row in p]))}
dev=np.load('data/geolife_development.npz')['paths'];test=np.load('data/geolife_test.npz')['paths'];freq=np.bincount(dev.ravel(),minlength=64);ties=np.flatnonzero(freq==freq.max());geo['development_only_population_prior']={'map_cells':ties.tolist(),'dev_peak':float(freq.max()/freq.sum()),'test_hit':float(np.isin(test,ties).mean()/len(ties)),'uniform_reference':1/64,'caution':'diagnostic unconditional stationary population prior, not an adaptive attacker rerun; not evidence of posterior cap violation'}
out['geolife']=geo
regions={}
for sc in ['static','walk','commute','geolife']:
 d={}
 for method in ['none_1','bsp_0.1']:
  bins={}
  with gzip.open(f'results/final/{sc}_adaptive_{method}.jsonl.gz','rt') as f:
   for line in f:
    row=json.loads(line)
    for e in row['events']:
     if not e['legitimate']:continue
     x0,x1,y0,y1=e['rectangle'];area=(x1-x0)*(y1-y0);v=bins.setdefault(area,{'tasks':0,'opportunities':0,'completed':0});v['tasks']+=1;v['opportunities']+=int(e['eligible'] and e['available']);v['completed']+=e['reported']
  d[method]=bins
 regions[sc]=d
out['normal_task_area_stratification']=regions
ss=list(csv.DictReader(open('results/recent_comparison/summary.csv')))
endpoints=[]
for sc in ['static','walk','commute','geolife']:
 none=next(s for s in ss if s['scenario']==sc and s['method']=='none')
 for method in ['bsp','pml','privic','random']:
  pts=[(float(s['utility']),float(s['hit'])) for s in ss if s['scenario']==sc and s['method']==method]
  for endpoints_on in [False,True]:
   ps=lower_hull(pts+([(0,1/64),(float(none['utility']),float(none['hit']))] if endpoints_on else []));v=float(np.interp(.5,[x for x,y in ps],[y for x,y in ps])) if ps[0][0]<=.5<=ps[-1][0] else None
   endpoints.append({'scenario':sc,'method':method,'add_common_endpoints':endpoints_on,'risk_at_0.5':v,'hull':ps})
out['envelope_endpoint_sensitivity']=endpoints
Path('research/reviews/reviewer_1_2026-09-17/checks_output.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='normal_task_area_stratification'},indent=2))
for sc,d in regions.items():
 b=d['bsp_0.1'];total=sum(v['completed'] for v in b.values());opp=sum(v['opportunities'] for v in b.values());big=sum(v['completed'] for a,v in b.items() if a>=32);smallopp=sum(v['opportunities'] for a,v in b.items() if a<=8);smallcomp=sum(v['completed'] for a,v in b.items() if a<=8)
 print(sc,'completed',total,'opps',opp,'>=32 share',big/total,'<=8 opps',smallopp,'<=8 completed',smallcomp)
