from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.parse,json,hashlib,subprocess
root=Path(__file__).resolve().parent
sources=[
 ('anonysense','10.1145/1378600.1378624','https://homes.luddy.indiana.edu/kapadia/papers/anonysense_mobisys08.pdf'),
 ('tmarkov','10.3390/s21072474','https://mdpi-res.com/d_attachment/sensors/sensors-21-02474/article_deploy/sensors-21-02474.pdf'),
 ('dual','10.1016/j.jnca.2018.09.007',None),
 ('crowdprivacy',None,'https://www.usenix.org/system/files/sec19-boukoros.pdf'),
 ('filters',None,'https://proceedings.neurips.cc/paper/6170-privacy-odometers-and-filters-pay-as-you-go-composition.pdf'),
 ('geo','10.1145/2508859.2516735','https://arxiv.org/pdf/1212.1984'),
 ('adaptive2023',None,'https://proceedings.mlr.press/v202/whitehouse23a/whitehouse23a.pdf'),
 ('p2ta','10.1016/j.sysarc.2019.01.005',None),
 ('fingerprint','10.1186/s42400-025-00539-2',None),
 ('blockchain','10.1016/j.pmcj.2025.102125',None),
 ('inference2026','10.1109/TMC.2026.3721057',None),
 ('bayesian','10.3982/TE4390','https://www.econtheory.org/ojs/index.php/te/article/viewFile/20211557/32395/934')]
def get(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'AcademicResearch/1.0'}),timeout=45).read()
def fetch(row):
 key,doi,url=row;status={'id':key,'doi':doi,'pdf_url':url,'checked':'2026-09-06','human_verified':False}
 if doi:
  try:
   data=get('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''))
   (root/(key+'_crossref.json')).write_bytes(data)
   msg=json.loads(data)['message'];status['title']=msg.get('title');status['authors']=msg.get('author');status['metadata_status']='Crossref fetched'
  except Exception as e:status['metadata_error']=str(e)
 if url:
  try:
   data=get(url)
   if not data.startswith(b'%PDF'):raise ValueError('not PDF')
   target=root/(key+'.pdf');target.write_bytes(data);status['sha256']=hashlib.sha256(data).hexdigest()
   subprocess.run(['pdftotext','-layout',str(target),str(root/(key+'.txt'))],check=True)
   status['fulltext_downloaded']=True
  except Exception as e:status['pdf_error']=str(e)
 print(key,status.get('metadata_status',''),status.get('fulltext_downloaded',False),status.get('pdf_error',''),flush=True)
 return status
with ThreadPoolExecutor(max_workers=6) as ex:records=list(ex.map(fetch,sources))
(root/'source_manifest.json').write_text(json.dumps(records,indent=2))
