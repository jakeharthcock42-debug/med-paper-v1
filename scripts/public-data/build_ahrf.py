"""Extract Mississippi county variables from HRSA AHRF 2024-2025 (NCHWA CSV) and merge into master -> master_county_ms.csv (adds ahrf_* columns).
Input: raw/ahrf/NCHWA-2024-2025+AHRF+COUNTY+CSV/AHRF2025.csv (https://data.hrsa.gov/data/download?data=AHRF)"""
import pandas as pd, numpy as np
f='raw/ahrf/NCHWA-2024-2025+AHRF+COUNTY+CSV/AHRF2025.csv'
a=pd.read_csv(f,dtype=str,low_memory=False); a=a[a.fips_st=='28'].copy()
num=lambda c: pd.to_numeric(a[c],errors='coerce')
o=pd.DataFrame({'fips':a.fips_st_cnty.str.zfill(5)})
o['ahrf_pop23']=num('popn_est_23'); o['ahrf_fem_pop23']=num('popn_fem_23')
o['ahrf_obgyn23']=num('md_nf_obgyn_gen_23')
o['ahrf_midwife_npi23']=num('apn_midwvs_npi_23')
o['ahrf_hosp_ob23']=num('stgh_obstetrc_care_23')
o['ahrf_ob_beds23']=num('stgh_obstetrcs_care_beds_23')
o['ahrf_nicu23']=num('stgh_neonat_icu_23')
o['ahrf_births3yr']=num('births_3yr_avg_23'); o['ahrf_births3yr_black']=num('births_3yr_bl_avg_23'); o['ahrf_births3yr_white']=num('births_3yr_wh_avg_23')
o['ahrf_preterm3yr']=num('births_pretrm_3yr_avg_23')
o['ahrf_infmort5yr']=num('inf_mort_rate_5yr_lt1_avg_23')
o['ahrf_dent_npi23']=num('dent_npi_23'); o['ahrf_dent_prv23']=num('dent_nf_prvprac_23')
o['ahrf_pcp_md23']=num('md_nf_prim_care_pc_excl_rsdnt_23'); o['ahrf_pcp_do23']=num('do_nf_prim_care_pc_excl_rsdnt_23')
o['ahrf_hpsa_prim25']=num('hpsa_prim_care_25'); o['ahrf_hpsa_dent25']=num('hpsa_dent_25')
o['ahrf_hospitals23']=num('stgh_23')
o['ahrf_nonmetro_ruc23']=num('rural_urban_contnm_23')
m=pd.read_csv('master_county_ms.csv',dtype={'fips':str})
m=m[[c for c in m.columns if not c.startswith('ahrf_')]].merge(o,on='fips',how='left',validate='1:1')
m['ahrf_pcp_total23']=m.ahrf_pcp_md23.fillna(0)+m.ahrf_pcp_do23.fillna(0)
m['obgyn_per10k_fem']=m.ahrf_obgyn23/m.ahrf_fem_pop23*1e4
m['dent_per10k']=m.ahrf_dent_prv23/m.ahrf_pop23*1e4
m['preterm_pct']=m.ahrf_preterm3yr/m.ahrf_births3yr*100
m['ob_hospital_any']=(m.ahrf_hosp_ob23>0).astype(float).where(m.ahrf_hosp_ob23.notna())
m.to_csv('master_county_ms.csv',index=False)
print(m[[c for c in m.columns if c.startswith('ahrf_')]+['obgyn_per10k_fem','dent_per10k','preterm_pct','ob_hospital_any']].describe().T.round(2).to_string())
print(m.ahrf_hpsa_prim25.value_counts(dropna=False).to_dict(), m.ahrf_hpsa_dent25.value_counts(dropna=False).to_dict())
print(m.ahrf_infmort5yr.notna().sum(), m.ahrf_preterm3yr.notna().sum())
