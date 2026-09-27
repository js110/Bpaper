"""Build a flat Elsevier Editorial Manager LaTeX submission staging directory."""
import argparse,json,re,shutil
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--paper',default='paper')
    ap.add_argument('--stage',default='build/pmc_submission_flat')
    args=ap.parse_args()
    paper=Path(args.paper);stage=Path(args.stage)
    if stage.exists():shutil.rmtree(stage)
    stage.mkdir(parents=True)
    main=(paper/'main.tex').read_text()
    graphics=re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',main)
    inputs=re.findall(r'\\input\{([^}]+)\}',main)
    copied=[]
    for name in ['references.bib','elsarticle.cls','elsarticle-num.bst']:
        src=paper/name
        if not src.exists():raise FileNotFoundError(src)
        shutil.copy2(src,stage/name);copied.append(name)
    for item in inputs:
        name=item if Path(item).suffix else item+'.tex'
        src=paper/name
        if not src.exists():raise FileNotFoundError(src)
        dest=Path(name).name
        shutil.copy2(src,stage/dest);copied.append(dest)
        if item!=Path(item).stem:
            main=main.replace('\\input{'+item+'}','\\input{'+Path(item).stem+'}')
    seen=set()
    for item in graphics:
        src=paper/item
        if not src.exists():raise FileNotFoundError(src)
        dest=Path(item).name
        if dest in seen and src.name!=dest:raise ValueError('graphic basename collision: '+dest)
        seen.add(dest)
        shutil.copy2(src,stage/dest);copied.append(dest)
        main=main.replace('{'+item+'}','{'+dest+'}')
    (stage/'main.tex').write_text(main)
    copied.append('main.tex')
    nested=[x for x in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',main) if '/' in x or '\\' in x]
    if nested:raise ValueError('nested graphics remain: '+repr(nested))
    manifest=dict(
        journal='Pervasive and Mobile Computing',
        source='paper/main.tex',
        flat_files=sorted(set(copied)),
        graphics=[Path(x).name for x in graphics],
        inputs=[Path(x).stem+'.tex' for x in inputs],
        no_subfolders=True)
    (stage/'SUBMISSION_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(manifest,indent=2))

if __name__=='__main__':main()
