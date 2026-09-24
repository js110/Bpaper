"""Public Bayesian channel and branch-safe participation. No true state access."""
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Task:
    task_id: str
    slot: int
    deadline: int
    rectangle: tuple[int, int, int, int]
    legitimate: bool = True
    def mask(self, side):
        x0,x1,y0,y1=self.rectangle
        if not (0<=x0<x1<=side and 0<=y0<y1<=side):
            raise ValueError('invalid half-open rectangle')
        x,y=np.meshgrid(np.arange(side),np.arange(side),indexing='ij')
        return ((x>=x0)&(x<x1)&(y>=y0)&(y<y1)).ravel()

@dataclass(frozen=True)
class Observation:
    task_id: str
    slot: int
    reported: bool


def normalize(b):
    b=np.asarray(b,dtype=float)
    s=b.sum()
    if s<=0 or np.any(b<0) or not np.all(np.isfinite(b)):
        raise ValueError('invalid or impossible belief')
    return b/s


def predict(b,side,move):
    """Reflecting, symmetric nearest-neighbour kernel (doubly stochastic)."""
    a=np.asarray(b).reshape(side,side)
    v=(1-move)*a.copy()
    v[:-1,:]+=move/4*a[1:,:];v[1:,:]+=move/4*a[:-1,:]
    v[:,:-1]+=move/4*a[:,1:];v[:,1:]+=move/4*a[:,:-1]
    v[0,:]+=move/4*a[0,:];v[-1,:]+=move/4*a[-1,:]
    v[:,0]+=move/4*a[:,0];v[:,-1]+=move/4*a[:,-1]
    return normalize(v.ravel())


def update(b,mask,alpha,q,reported):
    likelihood=alpha*q*np.asarray(mask,dtype=float)
    return normalize(b*(likelihood if reported else 1-likelihood))


def gates(b,masks,alpha,method,param,slot,rectangles=None):
    """Vectorized gates depending only on public belief, task, and slot."""
    masks=np.atleast_2d(masks).astype(float)
    count=len(masks)
    if method=='none':return np.ones(count)
    if method=='pml':
        from .recent_baselines import pml_gates
        return pml_gates(b,masks,alpha,param)
    if method=='random':return np.full(count,param)
    if method=='rate':return np.full(count,float(slot%int(param)==0))
    if method=='coarse':
        block=int(param)
        return np.asarray([all(v%block==0 for v in r) for r in rectangles],float)
    if method=='kl':
        # KL(post || prior) reduces exactly to the binary region partition.
        mass=(masks*b).sum(axis=1)
        allowed=-np.log(np.maximum(mass,1e-300))<=param+1e-12
        lo=np.zeros(count);hi=np.ones(count)
        for _ in range(30):
            mid=(lo+hi)/2;den=1-mid*alpha*mass
            inside=mass*(1-mid*alpha)/np.maximum(den,1e-300)
            outside=(1-mass)/np.maximum(den,1e-300)
            kl=inside*np.log(np.maximum(1-mid*alpha,1e-300)/np.maximum(den,1e-300))-outside*np.log(np.maximum(den,1e-300))
            ok=kl<=param;lo=np.where(ok,mid,lo);hi=np.where(ok,hi,mid)
        return lo*allowed
    if method not in ('bsp','positive_only'):
        raise ValueError(method)
    cap=max(float(param),float(np.max(b)))
    h=alpha*masks
    joint=h*b[None,:]
    mass=joint.sum(axis=1)
    positive_peak=np.divide(joint.max(axis=1),mass,out=np.zeros(count),where=mass>0)
    q=(positive_peak<=cap+1e-12).astype(float)
    if method=='positive_only':return q
    # b_i(1-q h_i) <= cap(1-q E[h])
    denom=cap*mass[:,None]-joint
    limits=np.divide(cap-b[None,:],denom,out=np.full_like(denom,np.inf),where=denom>1e-14)
    q=np.minimum(q,np.minimum(1,limits.min(axis=1)))
    return np.clip(q,0,1)


def binary_entropy(p):
    p=np.asarray(p,float)
    return -(p*np.log2(np.maximum(p,1e-300))+(1-p)*np.log2(np.maximum(1-p,1e-300)))


def choose_probe(b,masks,rectangles,alpha,method,param,slot):
    q=gates(b,masks,alpha,method,param,slot,rectangles)
    success=masks*(alpha*q[:,None])
    mass=(success*b).sum(axis=1)
    information=binary_entropy(mass)-(binary_entropy(success)*b).sum(axis=1)
    return int(np.argmax(information))


def posterior_metrics(b,true,side):
    order=np.argsort(-b,kind='stable')
    n=int(np.searchsorted(np.cumsum(b[order]),.95)+1)
    peak=b.max(); ties=np.flatnonzero(np.isclose(b,peak,rtol=1e-10,atol=1e-14))
    # Uniform tie breaking in expectation, avoiding cell-index bias.
    hit=float(true in ties)/len(ties)
    x,y=divmod(int(true),side)
    xy=np.array(np.unravel_index(ties,(side,side))).T
    error=float(np.linalg.norm(xy-np.array([x,y]),axis=1).mean())
    return dict(hit=hit,error_cells=error,peak=float(peak),logloss=float(-np.log(max(b[true],1e-300))),
                covered95=float(true in order[:n]),credible95=int(n),
                entropy=float(-(b*np.log2(np.maximum(b,1e-300))).sum()))

class PublicBelief:
    def __init__(self,side,move,alpha):
        self.side=side;self.move=move;self.alpha=alpha
        self.b=np.full(side*side,1/(side*side));self.seen=set()
    def observe(self,task,observation,q):
        if task.task_id!=observation.task_id or task.slot!=observation.slot:
            raise ValueError('task-observation mismatch')
        if task.task_id in self.seen:raise ValueError('duplicate observation')
        if task.deadline<task.slot:raise ValueError('expired task')
        self.b=update(self.b,task.mask(self.side),self.alpha,q,observation.reported)
        self.seen.add(task.task_id)
