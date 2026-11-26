import pandas as pd, numpy as np, re
R='raw/'
dra24="""Adams, Amite, Attala, Benton, Bolivar, Carroll, Claiborne, Coahoma, Copiah, Covington, DeSoto, Franklin, Grenada, Hinds, Holmes, Humphreys, Issaquena, Jefferson, Jasper, Jefferson Davis, Lafayette, Lawrence, Leflore, Lincoln, Marion, Marshall, Montgomery, Panola, Pike, Quitman, Sharkey, Simpson, Smith, Sunflower, Tallahatchie, Tate, Tippah, Tunica, Union, Walthall, Warren, Washington, Wilkinson, Yalobusha, Yazoo, Madison, Rankin"""
dra=[x.strip() for x in dra24.split(',')]
# CHR supplement (latest) ----
s=pd.read_csv(R+'chr_supp2026.csv',dtype=str,low_memory=False)
s=s[(s.statecode=='28')&(s.countycode!='000')].copy()
s['fips']=s.fipscode.str.zfill(5)
out=pd.DataFrame({'fips':s.fips,'county':s.county.str.replace(' County','')})
def num(c): return pd.to_numeric(s[c],errors='coerce')
m={'premature_death_ypll':'v001_rawvalue','prem_death_white':'v001_race_white','prem_death_black':'v001_race_black',
 'prem_mort_agadj':'v127_rawvalue','prem_mort_white':'v127_race_white','prem_mort_black':'v127_race_black',
 'life_exp':'v147_rawvalue','life_exp_white':'v147_race_white','life_exp_black':'v147_race_black',
 'lbw_pct':'v037_rawvalue','lbw_white':'v037_race_white','lbw_black':'v037_race_black',
 'infmort_rate':'v129_rawvalue','infmort_white':'v129_race_white','infmort_black':'v129_race_black',
 'teen_birth_rate':'v014_rawvalue','teen_white':'v014_race_white','teen_black':'v014_race_black',
 'pcp_per100k':'v004_rawvalue','dentist_per100k':'v088_rawvalue','mhp_per100k':'v062_rawvalue','otherpcp_per100k':'v131_rawvalue',
 'uninsured_pct':'v085_rawvalue','diabetes_prev_chr':'v060_rawvalue','obesity_pct':'v011_rawvalue','smoking_pct_chr':'v009_rawvalue',
 'inactivity_pct':'v070_rawvalue','prev_hosp_stays':'v005_rawvalue','prev_hosp_black':'v005_race_black','prev_hosp_white':'v005_race_white',
 'mammography_pct':'v050_rawvalue','mammo_black':'v050_race_black','mammo_white':'v050_race_white',
 'unemployment':'v023_rawvalue','income_inequality':'v044_rawvalue','flu_vacc':'v155_rawvalue','flu_black':'v155_race_black','flu_white':'v155_race_white'}
for k,v in m.items(): out[k]=num(v)
for v,k in [('v001','prem_death'),('v037','lbw'),('v129','infmort'),('v127','prem_mort')]:
    for r in ['black','white']:
        c=f'{v}_race_{r}_flag2'
        if c in s: out[f'{k}_{r}_flag']=s[c].values
# CHR 2025 for demographics
a=pd.read_csv(R+'chr2025.csv',dtype=str,low_memory=False).iloc[1:]
a=a[(a['State FIPS Code']=='28')&(a['County FIPS Code']!='000')].copy()
a['fips']=a['5-digit FIPS Code'].str.zfill(5)
d=pd.DataFrame({'fips':a.fips})
dm={'population':'Population raw value','pct_rural_chr':'% Rural raw value','pct_black_nh':'% Non-Hispanic Black raw value','pct_white_nh':'% Non-Hispanic White raw value',
 'pct_65plus':'% 65 and Older raw value','median_hh_income':'Median Household Income raw value','child_poverty':'Children in Poverty raw value',
 'child_poverty_black':'Children in Poverty (Black)','segregation_bw':'Residential Segregation - Black/White raw value','hs_completion':'High School Completion raw value',
 'some_college':'Some College raw value','pct_disability_func':'% Disability: Functional Limitations raw value','median_inc_black':'Median Household Income (Black)'}
for k,v in dm.items(): d[k]=pd.to_numeric(a[v],errors='coerce').values
out=out.merge(d,on='fips',how='left')
# RUCC
r=pd.read_csv(R+'rucc2023.csv',dtype=str,encoding='latin-1'); r=r[(r.State=='MS')&(r.Attribute=='RUCC_2023')]
out=out.merge(r[['FIPS','Value']].rename(columns={'FIPS':'fips','Value':'rucc2023'}),on='fips',how='left')
out['rucc2023']=out.rucc2023.astype(float)
out['nonmetro']=(out.rucc2023>=4).astype(int)
out['dra_county']=out.county.isin(dra).astype(int)
# PLACES
p=pd.read_csv(R+'places_ms_2025.csv',dtype={'countyfips':str})
keep={'hearing':'hearing_adjprev','dental':'dental_adjprev','colon_screen':'colon_screen_adjprev','mammouse':'mammouse_adjprev','cholscreen':'cholscreen_adjprev','checkup':'checkup_adjprev',
 'csmoking':'csmoking_adjprev','diabetes_pl':'diabetes_adjprev','chd':'chd_adjprev','stroke':'stroke_adjprev','bphigh':'bphigh_adjprev','obesity_pl':'obesity_adjprev','access2_uninsured':'access2_adjprev',
 'binge':'binge_adjprev','teethlost':'teethlost_adjprev','cancer_pl':'cancer_adjprev','foodinsecu':'foodinsecu_adjprev','lacktrpt':'lacktrpt_adjprev','copd':'copd_adjprev'}
pp=pd.DataFrame({'fips':p.countyfips.str.zfill(5)})
for k,v in keep.items(): pp['pl_'+k]=p[v].values
pp['pl_pop18']=p.totalpop18plus.values
out=out.merge(pp,on='fips',how='left')
out.to_csv('master_county_ms.csv',index=False)
print(out.shape, out.dra_county.sum(), out.nonmetro.sum(), out.rucc2023.isna().sum())
print(out.isna().sum()[out.isna().sum()>0].to_string())
# ---- unit scaling ----
for c in ['pcp_per100k','dentist_per100k','mhp_per100k','otherpcp_per100k']: out[c]=out[c]*100000
pc=['uninsured_pct','diabetes_prev_chr','obesity_pct','smoking_pct_chr','inactivity_pct','mammography_pct','mammo_black','mammo_white','unemployment','flu_vacc','flu_black','flu_white',
    'lbw_pct','lbw_white','lbw_black','pct_rural_chr','pct_black_nh','pct_white_nh','pct_65plus','child_poverty','child_poverty_black','hs_completion','some_college','pct_disability_func']
for c in pc: out[c]=out[c]*100
out=out.drop(columns=['pl_dental'])  # PLACES DENTAL values implausible (4.9-12.9%); excluded pending verification
out.to_csv('master_county_ms.csv',index=False)
print(out[['pcp_per100k','dentist_per100k','lbw_pct','uninsured_pct','pct_rural_chr','child_poverty']].describe().round(1).to_string())
