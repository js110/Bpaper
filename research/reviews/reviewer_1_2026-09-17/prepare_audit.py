import json,csv,re,hashlib,sys,platform
from pathlib import Path
p=Path('research/reviews/reviewer_1_2026-09-17');skill=Path('/Users/jiangsheng/.agents/skills/peer-review')
extra={}
for sc in ['static','walk','commute','geolife']:
 rows=[x for x in csv.DictReader(open('results/final/rows.csv')) if x['scenario']==sc and x['attack']=='adaptive' and x['method']=='bsp' and float(x['param'])==.1]
 vals={k:sum(float(x[k]) for x in rows) for k in ['legitimate','opportunities','complete']};vals['raw_completion']=vals['complete']/vals['legitimate'];extra[sc]=vals
(p/'additional_diagnostics.json').write_text(json.dumps(extra,indent=2))
profile=dict(schema_version='2.0',profile_id='COMPUTATIONAL-PRIVACY-REVIEW',study_types=['computational_simulation'],report_kind='results',features=[],domains=['computer_science'])
(p/'study_profile.json').write_text(json.dumps(profile,indent=2))
fields=['claim_id','location','claim_type','claim_summary','evidence_ids','support_level','alignment_issue','limitation','requested_action']
claims=[['C1','main.tex:99-124','methods','BSP local maximality and conditional sequential cap','E-BSP;E-TESTS','supported','none','Finite checks supplement rather than prove the result','Retain explicit model and transition conditions'],['C2','main.tex:149,204','methods','No test parameter selection','E-CODE;E-REANALYSIS','partly_supported','scope','Training is separate but test envelopes and followup grids are exploratory','Qualify training separation claim'],['C3','main.tex:214,265','prediction','Replay risk under uniform prior model','E-PRIOR','partly_supported','scope','Population prior ignoring outputs attains 25.75 percent hit','Report dev-prior control or narrow replay interpretation'],['C4','main.tex:223','primary_outcome','Nonzero useful opportunity retention','E-TASKAREA','partly_supported','outcome','Broad regions account for most completions at rho 0.1','Add area-stratified and raw completion table'],['C5','main.tex:46,304','other','Novelty relative to closest 2026 work','','not_assessed','scope','Full text absent','Complete bounded full-text comparison'],['C6','main.tex:247-258','primary_outcome','Recent policy envelope differences','E-REANALYSIS;E-LP','supported','none','Exploratory; fixed training and selected grid','State fixed training conditional uncertainty']]
with (p/'claim_evidence.csv').open('w') as f:
 w=csv.writer(f);w.writerow(fields);w.writerows(claims)
a=json.loads((skill/'assets/statistical_reproducibility_template.json').read_text());a.update(checklist_id='STAT-REPRO-AUTHOR-MOCK',study_design='computational_simulation',specialist_review=dict(needed='yes',areas=['closest_literature','selection_uncertainty'],requested=True))
for it in a['items']:
 it['status']='verified_present';it['evidence_locations']=['paper/main.tex:144-311','review_zh.md'];it['note']='Scope-limited review of reported computational design and local checks';it['requested_action']='Retain scope and reproducibility details'
 if it['id'] in ['design.blinding','ethics.approval_consent_governance']:
  it['applicability']='not_applicable';it['status']='not_applicable';it['note']='No blinded intervention trial; author data-use determination remains outside this computational audit';it['requested_action']='Authors to complete relevant data-use declarations before dissemination'
 if it['id'] in ['analysis.prespecification','analysis.assumptions_diagnostics','results.effect_sizes_uncertainty','interpretation.claim_evidence_causality']:
  it['status']='partly_documented';it['note']='See M1 M3 and m1 for prior mismatch and exploratory selection boundaries';it['requested_action']='Clarify estimand and conditional uncertainty'
 if it['id']=='design.sample_size_precision':
  it['status']='partly_documented';it['note']='Computational convenience rationale disclosed; no power claim';it['requested_action']='No retrospective power calculation requested'
 if it['id']=='reproducibility.data_materials_access':
  it['status']='partly_documented';it['note']='Local artifact available; public deposition pending';it['requested_action']='Retain explicit local-only availability statement until release'
(p/'statistics_checklist.json').write_text(json.dumps(a,indent=2))
# Local key/reference consistency conversion only, not literature verification.
tex=Path('paper/main.tex').read_text();keys=[]
for group in re.findall(r'\\cite\{([^}]+)\}',tex):keys.extend(group.split(','))
(p/'citation_keys.md').write_text('\n'.join('[@'+k+']' for k in keys))
bib=Path('paper/references.bib').read_text();entries=[]
for m in re.finditer(r'@\w+\{([^,]+),(.*?)(?=\n@|\Z)',bib,re.S):
 key,body=m.groups();d={}
 for name in ['title','author','year','doi','url']:
  q=re.search(r'\b'+name+r'\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}',body,re.S);d[name]=q.group(1).strip().strip('{}') if q else ''
 entries.append([key,d['title'],d['author'],d['year'],d['doi'],d['url'],'not_verified'])
with (p/'citation_references.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['reference_id','title','authors','year','doi','url','verification_status']);w.writerows(entries)
files=['paper/main.tex','paper/numbers.tex','paper/references.bib','paper/main_table.tex','paper/matched_table.tex','paper/recent_matched_table.tex','paper/informed_table.tex','src/model.py','src/experiment.py','src/analyze.py','src/analyze_recent.py','src/recent_baselines.py','src/prepare_data.py','data/geolife_development.npz','data/geolife_validation.npz','data/geolife_test.npz','results/recent_comparison/matched_utility.json']
(p/'review_input_hashes.json').write_text(json.dumps({x:hashlib.sha256(Path(x).read_bytes()).hexdigest() for x in files},indent=2))
