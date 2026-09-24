"""Deterministic GeoLife replay windows; no interpolation across missing minutes."""
import csv,hashlib,json,zipfile
from pathlib import Path
import numpy as np

BOUNDS=(39.8,40.1,116.2,116.6)

def minute_window(text,side=8,slots=48):
    lat0,lat1,lon0,lon1=BOUNDS
    points={}
    for line in text.splitlines()[6:]:
        r=line.split(',')
        if len(r)<7:continue
        try:
            lat,lon,days=float(r[0]),float(r[1]),float(r[4])
        except ValueError:continue
        if not(lat0<=lat<lat1 and lon0<=lon<lon1):continue
        minute=int(np.floor(days*1440+1e-6))
        # First in-bounds sample per minute; no inferred intermediate movement.
        if minute not in points:points[minute]=(lat,lon)
    keys=sorted(points);run=[]
    for k in keys:
        if run and k!=run[-1]+1:run=[]
        run.append(k)
        if len(run)==slots:
            coords=np.array([points[i] for i in run])
            x=np.minimum(side-1,((coords[:,0]-lat0)/(lat1-lat0)*side).astype(int))
            y=np.minimum(side-1,((coords[:,1]-lon0)/(lon1-lon0)*side).astype(int))
            return x*side+y,coords,run[0]
    return None

def main():
    source=Path('data/geolife.zip');z=zipfile.ZipFile(source)
    members=sorted(n for n in z.namelist() if n.endswith('.plt'))
    byuser={}
    for name in members:
        user=int(name.split('/Data/')[1].split('/')[0]);byuser.setdefault(user,[]).append(name)
    selected=[];excluded=[]
    for user,files in sorted(byuser.items()):
        found=None
        for name in files:
            found=minute_window(z.read(name).decode('utf-8-sig',errors='replace'))
            if found is not None:break
        if found is None:excluded.append({'user':user,'reason':'no 48 consecutive in-bounds one-minute samples in one file'});continue
        path,coords,start=found
        selected.append(dict(user=user,member=name,start_minute=start,path=path,coords=coords,split='development' if user%5==0 else ('validation' if user%5==1 else 'test')))
    for split in ['development','validation','test']:
        group=[r for r in selected if r['split']==split]
        np.savez_compressed(f'data/geolife_{split}.npz',users=np.array([r['user'] for r in group]),paths=np.array([r['path'] for r in group]),coords=np.array([r['coords'] for r in group]))
    dev=[r for r in selected if r['split']=='development']
    change=float(np.mean([np.mean(np.diff(r['path'])!=0) for r in dev]))
    manifest=dict(source_url='https://download.microsoft.com/download/F/4/8/F4894AA5-FDBC-481E-9285-D5F8C4C4F039/Geolife%20Trajectories%201.3.zip',
        source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),bounds=BOUNDS,side=8,slots=48,slot_seconds=60,
        rule='First lexicographic eligible file and first 48 consecutive minute bins per user; first in-bounds observation per minute; no interpolation.',
        split_rule='user modulo 5: 0 development, 1 validation, 2/3/4 test',
        development_change_probability=change,fit_model='Reflecting four-neighbour walk fitted only to development change rate; jump direction/distance not fitted.',
        users_total=len(byuser),counts={s:sum(r['split']==s for r in selected) for s in ['development','validation','test']},
        selected=[{k:v for k,v in r.items() if k not in ['path','coords']} for r in selected],excluded=excluded)
    Path('data/manifest.json').write_text(json.dumps(manifest,indent=2));print(json.dumps({k:manifest[k] for k in ['users_total','counts','development_change_probability']}))
if __name__=='__main__':main()
