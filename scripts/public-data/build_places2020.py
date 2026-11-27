"""Add CDC PLACES 2023 release (BRFSS 2020 based) dental-visit and all-teeth-lost, age-adjusted, county, to master_county_ms.csv.
Also colorectal screening (ages 50-75 in this release; 45-75 in 2025) and mammography (50-74), BRFSS 2020, as a sensitivity set.
Why: the PLACES 2024/2025 releases carry MS DENTAL values of 4.9-12.9% (implausible; other states 39-66%); see data-sources.md."""
import pandas as pd, requests, io
base='https://data.cdc.gov/resource/h3ej-a9ec.csv'
def get(meas):
    q={'stateabbr':'MS','measureid':meas,'datavaluetypeid':'AgeAdjPrv','$limit':'100'}
    d=pd.read_csv(io.StringIO(requests.get(base,params=q,timeout=60).text),dtype={'locationid':str})
    return d.set_index('locationid').data_value.rename
m=pd.read_csv('master_county_ms.csv',dtype={'fips':str})
for meas,col in [('DENTAL','pl20_dental'),('TEETHLOST','pl20_teethlost'),('COLON_SCREEN','pl20_colon'),('MAMMOUSE','pl20_mammo')]:
    s=get(meas)(col); m=m[[c for c in m.columns if c!=col]].merge(s,left_on='fips',right_index=True,how='left')
m.to_csv('master_county_ms.csv',index=False)
print(m[['pl20_dental','pl20_teethlost','pl20_colon','pl20_mammo']].describe().round(1))
