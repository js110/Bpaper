import unittest
import numpy as np
from src.model import *
from src.experiment import candidates,path_for,simulate

class ChannelTests(unittest.TestCase):
    def test_silence_is_not_false(self):
        b=np.array([.5,.5]);v=update(b,[1,0],.5,1,False)
        np.testing.assert_allclose(v,[1/3,2/3])
    def test_success_independent_of_thinning(self):
        b=np.array([.2,.3,.5]);m=[1,1,0]
        np.testing.assert_allclose(update(b,m,.7,.1,True),update(b,m,.7,1,True))
    def test_zero_gate_and_zero_delivery(self):
        b=np.array([.3,.7])
        np.testing.assert_allclose(update(b,[1,0],.5,0,False),b)
        np.testing.assert_allclose(update(b,[1,0],0,1,False),b)
    def test_transition_mass_and_peak(self):
        b=np.random.default_rng(1).dirichlet(np.ones(64))
        for m in [0,.5,1]:
            v=predict(b,8,m);self.assertAlmostEqual(v.sum(),1);self.assertLessEqual(v.max(),b.max()+1e-12)
    def test_branch_bound_and_maximality(self):
        rng=np.random.default_rng(11)
        for _ in range(500):
            b=rng.dirichlet(np.ones(16)*3);mask=rng.random(16)<.5;alpha=float(rng.uniform(.1,.95));rho=float(rng.uniform(.08,.4));cap=max(rho,b.max())
            q=gates(b,mask,alpha,'bsp',rho,0)[0]
            for r in [True,False]:
                pr=q*alpha*np.dot(b,mask);pr=pr if r else 1-pr
                if pr>1e-12:self.assertLessEqual(update(b,mask,alpha,q,r).max(),cap+1e-9)
            if q<.999 and np.dot(b,mask)>0:
                q2=min(1,q+1e-5)
                self.assertTrue(any(update(b,mask,alpha,q2,r).max()>cap-1e-10 for r in [True,False]))
    def test_positive_only_can_leak_silence(self):
        b=np.array([.2,.2,.2,.4]);m=[1,1,1,0]
        self.assertEqual(gates(b,m,.9,'positive_only',.4,0)[0],1)
        self.assertGreater(update(b,m,.9,1,False).max(),.4)
        self.assertAlmostEqual(gates(b,m,.9,'bsp',.4,0)[0],0)
    def test_boundaries_duplicates_expiry(self):
        t=Task('a',0,0,(0,1,0,1));self.assertEqual(t.mask(2).sum(),1)
        b=PublicBelief(2,0,.5);o=Observation('a',0,False);b.observe(t,o,1)
        with self.assertRaises(ValueError):b.observe(t,o,1)
        with self.assertRaises(ValueError):Task('b',0,0,(0,3,0,1)).mask(2)
        with self.assertRaises(ValueError):PublicBelief(2,0,.5).observe(Task('b',1,0,(0,1,0,1)),Observation('b',1,False),1)
    def test_prior_tie_unbiased(self):
        for x in range(16):self.assertAlmostEqual(posterior_metrics(np.full(16,1/16),x,4)['hit'],1/16)
    def test_public_state_no_ground_truth_fields(self):
        self.assertEqual(set(Observation.__dataclass_fields__),{'task_id','slot','reported'})
        self.assertNotIn('truth',PublicBelief(2,0,.5).__dict__)
    def test_seed_reproducibility(self):
        np.testing.assert_array_equal(path_for(1,2,8,64,'walk',.3),path_for(1,2,8,64,'walk',.3))
if __name__=='__main__':unittest.main()
