"""Generate manuscript numbers and displays from immutable experiment outputs."""
import csv,gzip,json,hashlib,shutil,zipfile,html
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def main():
    paper=ROOT/'paper';summary=list(csv.DictReader((ROOT/'results/combined/analysis/summary.csv').open()))
    registry=[];macros=[]
    def macro(name,value,source):
        macros.append('\\newcommand{\\'+name+'}{'+value+'}')
        registry.append(dict(id=name,value=value,source=source,human_verified=False))
    for scenario in ['static','walk','commute','geolife']:
        for method,par in [('none',1),('bsp',.1),('positive_only',.1),('random',.5)]:
            r=next(r for r in summary if r['scenario']==scenario and r['method']==method and float(r['param'])==par and r['attack']=='adaptive')
            prefix=scenario.capitalize()+{'none':'None','bsp':'Bsp','positive_only':'Ablation','random':'Random'}[method]
            for k,label in [('hit','Hit'),('utility','Retention'),('covered95','Coverage'),('peak','Peak')]:
                macro(prefix+label,f'{100*float(r[k]):.1f}',f'results/combined/analysis/summary.csv:{r["condition"]}:{k} percent')
    match=json.loads((ROOT/'results/combined/analysis/matched_utility.json').read_text())
    lines=[r'\begin{tabular}{llrrr}',r'\toprule',r'Scenario & Comparator & BSP hit & Other hit & Difference [95\% CI] \\',r'\midrule']
    for sc in ['static','walk','commute','geolife']:
        for rival in ['random','kl']:
            r=next(r for r in match if r['scenario']==sc and r['comparator']==rival and r['target_utility']==.5)
            nums=[100*r[k] for k in ['bsp_hit','comparator_hit','difference','low','high']]
            lines.append(f'{sc.capitalize()} & '+('Random' if rival=='random' else 'KL')+f' & {nums[0]:.2f} & {nums[1]:.2f} & {nums[2]:+.2f} [{nums[3]:+.2f}, {nums[4]:+.2f}] '+r'\\')
    lines +=[r'\bottomrule',r'\end{tabular}'];(paper/'matched_table.tex').write_text('\n'.join(lines))
    lines=[r'\begin{tabular}{lrrrr}',r'\toprule',r'Client mismatch & Retention & MAP hit & Above cap & Largest peak \\',r'\midrule']
    detail=[]
    stress=list(csv.DictReader((ROOT/'results/informed/analysis/summary.csv').open()))
    for cid,label in [('alpha_model_0.3',r'$\widehat\alpha=0.3$'),('alpha_model_0.9',r'$\widehat\alpha=0.9$'),('move_model_0.05',r'$\widehat v=0.05$'),('move_model_0.8',r'$\widehat v=0.8$')]:
        path=ROOT/f'results/informed/informed_{cid}_bsp.jsonl.gz';events=[e for l in gzip.open(path,'rt') for e in json.loads(l)['events']]
        peaks=np.array([max(e['belief']) for e in events]);r=next(r for r in stress if r['condition']=='informed_'+cid+'_bsp')
        f=float(np.mean(peaks>.1+1e-9));mx=float(peaks.max());cl=max(e['client_peak'] for e in events)
        lines.append(label+f" & {float(r['utility']):.3f} & {float(r['hit']):.3f} & {100*f:.1f}\\% & {mx:.3f} "+r'\\')
        detail.append(dict(condition=r['condition'],fraction_above_cap=f,maximum_peak=mx,client_maximum=cl,events=len(events),source=str(path.relative_to(ROOT)),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    lines +=[r'\bottomrule',r'\end{tabular}'];(paper/'informed_table.tex').write_text('\n'.join(lines));(ROOT/'results/informed/analysis/cap_audit.json').write_text(json.dumps(detail,indent=2))
    (paper/'numbers.tex').write_text('\n'.join(macros)+'\n');(ROOT/'research/numeric_registry.json').write_text(json.dumps(registry,indent=2))
    for source in ['combined/analysis/tradeoff','combined/analysis/calibration','combined/analysis/attacks','sensitivity/analysis/sensitivity','informed/analysis/informed']:
        for ext in ['pdf','png']:shutil.copyfile(ROOT/('results/'+source+'.'+ext),paper/(Path(source).name+'.'+ext))
    shutil.copyfile(ROOT/'results/combined/analysis/main_table.tex',paper/'main_table.tex')
    # Verified Crossref records plus official conference/dataset metadata.
    entries=[]
    for key in ['tmarkov','bayesian','fingerprint','inference2026']:
        d=json.loads((ROOT/f'literature/{key}_crossref.json').read_text());d=d.get('message',d)
        title=': '.join(d.get('title',[])+d.get('subtitle',[]));title=html.unescape(title).replace('&',r'\&')
        if key=='anonysense':title='AnonySense: Privacy-Aware People-Centric Sensing'
        kind='inproceedings' if key in ['anonysense','geo'] else 'article'
        fields={'author':' and '.join(a.get('given','')+' '+a['family'] for a in d['author']),'title':'{'+title+'}',
                'year':str(d['published']['date-parts'][0][0]),'doi':d['DOI'],
                'booktitle' if kind=='inproceedings' else 'journal':html.unescape(d['container-title'][0]).replace('&',r'\&')}
        for k,bk in [('volume','volume'),('issue','number'),('page','pages')]:
            if d.get(k):fields[bk]=d[k].replace('-','--') if k=='page' else d[k]
        if key=='fingerprint':fields['pages']='105'
        if key=='inference2026' and not d.get('volume'):fields['note']=', Early Access; volume not assigned in the verified record'
        entries.append('@'+kind+'{'+key+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}')
    entries.append(r'''@inproceedings{adaptive2023,
 author={Justin Whitehouse and Aaditya Ramdas and Ryan Rogers and Steven Wu},
 title={{Fully-Adaptive Composition in Differential Privacy}},
 booktitle={Proceedings of the 40th International Conference on Machine Learning},series={Proceedings of Machine Learning Research},volume={202},pages={36990--37007},year={2023},
 url={https://proceedings.mlr.press/v202/whitehouse23a.html}}
''')
    for key in ['pml','privic','fedsense']:
        d=json.loads((ROOT/f'literature/recent/{key}_crossref.json').read_text())['message']
        fields={'author':' and '.join(a.get('given','')+' '+a['family'] for a in d['author']),
                'title':'{'+html.unescape(d['title'][0])+'}','year':str(d['published']['date-parts'][0][0]),
                'journal':html.unescape(d['container-title'][0]),'doi':d['DOI']}
        for k in ['volume','issue','page']:
            if d.get(k):fields[{'volume':'volume','issue':'number','page':'pages'}[k]]=d[k].replace('-','--') if k=='page' else d[k]
        entries.append('@article{'+key+('2025' if key=='fedsense' else '2024')+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}')
    (paper/'references.bib').write_text('\n\n'.join(entries)+'\n'+(ROOT/'literature/dataset_references.bib').read_text())
    z=zipfile.ZipFile(paper/'official_elsarticle.zip')
    for name in ['elsarticle-num.bst','elsarticle.dtx','elsarticle.ins','elsarticle-template-num.tex']:
        target=paper/(name if name!='elsarticle-template-num.tex' else 'official-template-num.tex');target.write_bytes(z.read('elsarticle/'+name))
    print('Generated paper assets and',len(registry),'numeric records')
if __name__=='__main__':main()
