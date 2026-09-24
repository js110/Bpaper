import copy,gzip,json,unittest
from pathlib import Path
import numpy as np
from src.model import gates,update
from src.experiment import simulate,candidates,path_for
from src.prepare_data import minute_window

class PipelineTests(unittest.TestCase):
    def test_kl_branches_and_maximality(self):
        rng=np.random.default_rng(29)
        for _ in range(100):
            b=rng.dirichlet(np.ones(16));mask=rng.random(16)<.6;alpha=.7;kappa=float(rng.uniform(.05,2))
            q=gates(b,mask,alpha,'kl',kappa,0)[0]
            def divergence(q,r):
                p=update(b,mask,alpha,q,r);nz=p>0
                return np.sum(p[nz]*np.log(p[nz]/b[nz]))
            if q>0:self.assertLessEqual(divergence(q,True),kappa+1e-8)
            self.assertLessEqual(divergence(q,False),kappa+1e-8)
            if q<.999 and np.dot(b,mask)>0:
                self.assertGreater(max(divergence(q+1e-5,r) for r in [True,False]),kappa-1e-8)
    def test_missing_minute_not_interpolated(self):
        def fixture(minutes):
            return '\n'.join(['header']*6+[f'39.9,116.3,0,0,{m/1440:.12f},2008-01-01,00:00:00' for m in minutes])
        self.assertIsNone(minute_window(fixture([1,2,4]),slots=3))
        self.assertIsNotNone(minute_window(fixture([1,2,3]),slots=3))
    def test_data_split_disjoint(self):
        groups=[set(np.load(f'data/geolife_{s}.npz')['users']) for s in ['development','validation','test']]
        for i in range(3):
            for j in range(i):self.assertFalse(groups[i]&groups[j])
    def test_shared_normal_tasks_and_exogenous_draws(self):
        c=json.loads(Path('configs/final.json').read_text())['conditions'][0]
        r,m=candidates(8);path=path_for(1000,0,8,48,c['scenario'],c['move_true'])
        _,a=simulate(c,1000,0,path,r,m,48,8,True)
        c=copy.deepcopy(c);c.update(method='bsp',param=.1)
        _,b=simulate(c,1000,0,path,r,m,48,8,True)
        for x,y in zip(a,b):
            self.assertEqual(x['legitimate'],y['legitimate']);self.assertEqual(x['available'],y['available'])
            if x['legitimate']:self.assertEqual(x['rectangle'],y['rectangle'])
    def test_default_replay_matches_archived_numerics(self):
        cfg=json.loads(Path('configs/final.json').read_text());c=next(c for c in cfg['conditions'] if c['scenario']=='walk' and c['method']=='bsp' and c['param']==.1 and c['attack']=='adaptive')
        r,m=candidates(8);path=path_for(1000,0,8,48,'walk',.3)
        _,events=simulate(c,1000,0,path,r,m,48,8,True)
        with gzip.open('results/final/'+c['id']+'.jsonl.gz','rt') as f:old=json.loads(next(f))['events']
        for a,b in zip(events,old):
            self.assertEqual(a['reported'],b['reported']);self.assertEqual(tuple(a['rectangle']),tuple(b['rectangle']))
            np.testing.assert_allclose(a['belief'],b['belief'],rtol=1e-13,atol=1e-14)
if __name__=='__main__':unittest.main()
