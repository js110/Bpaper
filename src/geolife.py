"""GeoLife split loading with exact-coordinate decontamination.

The committed NPZ files are treated as raw deterministic caches.  Effective
development/validation/test splits are formed in that order and later exact
48-slot coordinate duplicates are dropped.  Equality of coarse grid-state
paths alone is deliberately not a duplicate criterion.
"""
import hashlib
import json
from pathlib import Path
import numpy as np

SPLIT_ORDER=("development","validation","test")

def coordinate_fingerprint(coords):
    """Stable SHA-256 fingerprint for an exact coordinate window."""
    a=np.asarray(coords,dtype=np.float64)
    a=np.ascontiguousarray(a.astype(">f8",copy=False))
    return hashlib.sha256(a.tobytes()).hexdigest()

def _read_npz(path):
    p=Path(path)
    with np.load(p) as data:
        return {k:np.array(data[k],copy=True) for k in ("users","paths","coords")}

def effective_geolife_splits(paths=None):
    """Return decontaminated splits and records for dropped exact duplicates.

    Split precedence is development, then validation, then test.  If two users
    have exactly the same 48-slot GPS coordinate window, only the earliest
    split's copy is retained.  This prevents train/validation/test leakage
    without treating coarse 8x8 state-path collisions as duplicate trajectories.
    """
    if paths is None:
        paths={s:Path("data")/f"geolife_{s}.npz" for s in SPLIT_ORDER}
    else:
        paths={s:Path(p) for s,p in paths.items()}
    raw={s:_read_npz(paths[s]) for s in SPLIT_ORDER if s in paths}
    seen={};out={};dropped=[]
    for split in SPLIT_ORDER:
        if split not in raw:continue
        data=raw[split];keep=[]
        for i,(user,coords) in enumerate(zip(data["users"],data["coords"])):
            fp=coordinate_fingerprint(coords)
            if fp in seen:
                prior=seen[fp]
                dropped.append(dict(
                    split=split,user=int(user),fingerprint=fp,
                    duplicate_of_split=prior["split"],
                    duplicate_of_user=prior["user"]))
                continue
            seen[fp]=dict(split=split,user=int(user))
            keep.append(i)
        idx=np.asarray(keep,dtype=int)
        out[split]={k:v[idx] for k,v in data.items()}
    return out,dropped

def load_effective_geolife(path):
    """Load one split, decontaminating against all earlier standard splits."""
    p=Path(path)
    split=None
    for s in SPLIT_ORDER:
        if p.name==f"geolife_{s}.npz":
            split=s;break
    if split is None:
        return _read_npz(p)

    upto=SPLIT_ORDER.index(split)
    paths={}
    for s in SPLIT_ORDER[:upto+1]:
        q=p.with_name(f"geolife_{s}.npz")
        if q.exists():paths[s]=q
    if split not in paths:
        paths[split]=p
    splits,_=effective_geolife_splits(paths)
    return splits[split]


def effective_development_change_probability(paths=None):
    """Mean per-window coarse-state change rate on the effective development split."""
    splits,_=effective_geolife_splits(paths)
    dev=np.asarray(splits["development"]["paths"])
    if len(dev)==0:
        raise ValueError("effective development split is empty")
    return float(np.mean([np.mean(np.diff(path)!=0) for path in dev]))

def decontamination_audit(paths=None):
    """Machine-readable audit of raw caches versus effective exact-coordinate splits."""
    if paths is None:
        paths={s:Path("data")/f"geolife_{s}.npz" for s in SPLIT_ORDER}
    else:
        paths={s:Path(p) for s,p in paths.items()}
    raw={s:_read_npz(paths[s]) for s in SPLIT_ORDER if s in paths}
    effective,dropped=effective_geolife_splits(paths)
    return {
        "rule":"SHA-256 of the complete float64 GPS coordinate window; retain first occurrence in development -> validation -> test order; coarse 8x8 state-path equality alone is not a duplicate criterion.",
        "raw_counts":{s:int(len(raw[s]["users"])) for s in raw},
        "effective_counts":{s:int(len(effective[s]["users"])) for s in effective},
        "development_change_probability":effective_development_change_probability(paths),
        "dropped":dropped,
    }

if __name__=="__main__":
    print(json.dumps(decontamination_audit(),indent=2))
