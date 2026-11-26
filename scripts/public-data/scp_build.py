import pandas as pd, glob, os, re, sys
sys.path.insert(0,'.')
from scp_parse import parse
rows=[]
cmap={'oral':'Oral cavity & pharynx','crc':'Colon & rectum','breast':'Breast (female)','cervix':'Cervix','lung':'Lung & bronchus'}
for f in sorted(glob.glob('raw/scp/*.csv')):
    b=os.path.basename(f)[:-4]
    if b.startswith('scp'): continue
    t,d=parse(f)
    parts=t.split(' | ')
    cancer=parts[1].split(' (')[0] if ' (' in parts[1] else parts[1].split(',')[0]
    period=re.search(r'(20\d\d-20\d\d)',parts[1]).group(1)
    pop=parts[2].strip().strip('"')
    typ='incidence' if 'Incidence' in parts[0] else 'mortality'
    late='Late Stage' in parts[1]
    cols=list(d.columns)
    rate=[c for c in cols if c.startswith('Age-Adjusted')][0]
    lo=[c for c in cols if c.startswith('Lower') ][0]
    hi=[c for c in cols if c.startswith('Upper')][0]
    cnt=[c for c in cols if c=='Average Annual Count'][0]
    pl=[c for c in cols if c.startswith('Percent of Cases')]
    rc=[c for c in cols if 'Rural-Urban' in c][0]
    o=pd.DataFrame({'dataset':b,'cancer':cancer,'type':typ+('_late_stage' if late else ''),'population':pop,'period':period,
      'county':d.County.str.replace(r'\(\d+\)','',regex=True).str.replace(' County','').str.strip(),'fips':d.FIPS.str.zfill(5),
      'scp_rural_urban':d[rc],'rate_per_100k':pd.to_numeric(d[rate].str.strip(),errors='coerce'),
      'ci_lo':pd.to_numeric(d[lo].str.strip(),errors='coerce'),'ci_hi':pd.to_numeric(d[hi].str.strip(),errors='coerce'),
      'avg_annual_count':pd.to_numeric(d[cnt],errors='coerce'),
      'pct_late':pd.to_numeric(d[pl[0]],errors='coerce') if pl else pd.NA})
    rows.append(o)
allr=pd.concat(rows)
allr.to_csv('scp_all_long.csv',index=False)
print(allr.groupby(['dataset']).rate_per_100k.apply(lambda s:s.notna().sum()).to_string())
print(allr[allr.fips.isin(['28000','00000'])][['dataset','population','fips','rate_per_100k','ci_lo','ci_hi','avg_annual_count','pct_late']].to_string())
