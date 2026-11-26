"""Paper 01 county-level merge + tests. Inputs: raw/. Outputs: out/ (merged csv, results.json, tables)."""
import pandas as pd, numpy as np, json
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
R='raw/'
# --- PLACES (2025 release; BRFSS 2023)
p=pd.read_csv(R+'places_ms_hearing_2025release.csv',dtype={'locationid':str})
assert (p.measureid=='HEARING').all() and p.year.eq(2023).all()
pc=p[p.datavaluetypeid=='CrdPrv'].set_index('locationid'); pa=p[p.datavaluetypeid=='AgeAdjPrv'].set_index('locationid')
places=pd.DataFrame({'fips':pc.index,'county':pc.locationname.values,
  'places_hearing_crude':pc.data_value.values,'places_hearing_crude_lo':pc.low_confidence_limit.values,'places_hearing_crude_hi':pc.high_confidence_limit.values,
  'places_pop18plus':pc.totalpop18plus.values}).set_index('fips')
places['places_hearing_ageadj']=pa.data_value; places['places_hearing_ageadj_lo']=pa.low_confidence_limit; places['places_hearing_ageadj_hi']=pa.high_confidence_limit
# --- ACS 5-year 2020-2024 (table-based SF)
def acs(t):
    d=pd.read_csv(R+f'acsdt5y2024-{t}.dat',sep='|',dtype=str)
    d=d[d.GEO_ID.str.startswith('0500000US28')].copy(); d['fips']=d.GEO_ID.str[-5:]; return d.set_index('fips')
b=acs('b18102'); f=lambda d,v: d[f'{v[:6]}_E{v[7:]}'].astype(float)
hearing_lines=[4,7,10,13,16,19,23,26,29,32,35,38]
hear=sum(b[f'B18102_E{n:03d}'].astype(float) for n in hearing_lines)
tot=b['B18102_E001'].astype(float)
# 65+ strata: male 015-017, 018-020; female 034-036, 037-039
n65=sum(b[f'B18102_E{n:03d}'].astype(float) for n in [15,18,34,37])
h65=sum(b[f'B18102_E{n:03d}'].astype(float) for n in [16,19,35,38])
acsd=pd.DataFrame({'acs_civ_noninst_pop':tot,'acs_hearing_n':hear,'acs_hearing_pct':100*hear/tot,'acs_pct_65plus':100*n65/tot,'acs_hearing_pct_65plus':100*h65/n65})
r=acs('b02001'); acsd['acs_pct_black_alone']=100*r['B02001_E003'].astype(float)/r['B02001_E001'].astype(float)
q=acs('b17001'); acsd['acs_pct_poverty']=100*q['B17001_E002'].astype(float)/q['B17001_E001'].astype(float)
# --- CHR 2025
c=pd.read_csv(R+'analytic_data2025_v3.csv',skiprows=[1],dtype={'5-digit FIPS Code':str},low_memory=False)
c=c[(c['State Abbreviation']=='MS')&(c['County FIPS Code']!=0)].set_index('5-digit FIPS Code')
chr_=pd.DataFrame({'chr_pcp_per100k':1e5*c['Primary Care Physicians numerator']/c['Primary Care Physicians denominator'],'chr_pcp_n':c['Primary Care Physicians numerator'],
 'chr_uninsured_pct_u65':100*c['Uninsured raw value'],'chr_pct_rural':100*c['% Rural raw value'],'chr_pct_nh_black':100*c['% Non-Hispanic Black raw value'],
 'chr_child_poverty_pct':100*c['Children in Poverty raw value'],'chr_median_hh_income':c['Median Household Income raw value'],
 'chr_population':c['Population raw value'],'chr_pct_65plus':100*c['% 65 and Older raw value']})
m=places.join(acsd,how='outer').join(chr_,how='outer')
m['county']=m['county'].fillna(c['Name'].str.replace(' County',''))
m['rural_ge50']=(m.chr_pct_rural>=50).astype(int)
m=m.reset_index().rename(columns={'index':'fips'})
assert len(m)==82 and m.fips.is_unique, len(m)
m.round(4).to_csv('out/ms_county_merged.csv',index=False)
res={'n_counties':len(m),'missing':m.isna().sum()[m.isna().sum()>0].to_dict(),'missing_counties':m[m.isna().any(axis=1)][['fips','county']].values.tolist()}
D=m.describe().T[['count','mean','std','min','50%','max']]; D.to_csv('out/descriptives.csv')
res['desc']=D.round(3).to_dict('index')
# --- tests
y='places_hearing_ageadj'
tests=[('chr_pct_rural','H-C1 % rural (CHR 2020 Census)'),('rural_ge50','(binary)'),('acs_pct_black_alone','H-C2 % Black alone (ACS 2020-24)'),
 ('acs_pct_poverty','H-C3 % below poverty (ACS 2020-24)'),('chr_pcp_per100k','H-C4 PCP per 100k (CHR/AMA 2021)'),('chr_uninsured_pct_u65','H-C5 % uninsured <65 (SAHIE 2022)')]
rows=[]
for x,lab in tests[:1]+tests[2:]:
    d=m[[y,x]].dropna(); rho,pv=stats.spearmanr(d[x],d[y]); rows.append(dict(hyp=lab,outcome=y,predictor=x,n=len(d),spearman_rho=rho,p=pv))
# alt outcomes
for yy in ['places_hearing_crude','acs_hearing_pct','acs_hearing_pct_65plus']:
    for x,lab in tests[:1]+tests[2:]:
        d=m[[yy,x]].dropna(); rho,pv=stats.spearmanr(d[x],d[yy]); rows.append(dict(hyp=lab+' [sens]',outcome=yy,predictor=x,n=len(d),spearman_rho=rho,p=pv))
T=pd.DataFrame(rows)
prim=T[T.outcome==y].copy(); prim['p_holm']=np.minimum(1,(prim.p.rank(method='first').pipe(lambda r:(len(prim)-r+1))*prim.p)).values
# proper Holm
o=prim.p.sort_values().index; k=len(prim); run=0; hp={}
for i,idx in enumerate(o):
    run=max(run,min(1,(k-i)*prim.p[idx])); hp[idx]=run
prim['p_holm']=pd.Series(hp)
T=T.merge(prim[['hyp','outcome','p_holm']],on=['hyp','outcome'],how='left'); T.to_csv('out/spearman_tests.csv',index=False)
res['spearman']=T.round(5).to_dict('records')
# rural vs non-rural
rv=[]
for yy in [y,'places_hearing_crude','acs_hearing_pct','acs_hearing_pct_65plus']:
    a=m.loc[m.rural_ge50==1,yy].dropna(); n=m.loc[m.rural_ge50==0,yy].dropna()
    u=stats.mannwhitneyu(a,n,alternative='two-sided'); t=stats.ttest_ind(a,n,equal_var=False)
    rv.append(dict(outcome=yy,n_rural=len(a),n_nonrural=len(n),mean_rural=a.mean(),sd_rural=a.std(),mean_nonrural=n.mean(),sd_nonrural=n.std(),median_rural=a.median(),median_nonrural=n.median(),diff_means=a.mean()-n.mean(),mwu_p=u.pvalue,welch_p=t.pvalue))
# fully rural (100%) vs others
a=m.loc[m.chr_pct_rural==100,y]; n=m.loc[m.chr_pct_rural<100,y]; res['fully_rural']=dict(n_100=len(a),n_lt100=len(n),mean_100=a.mean(),mean_lt100=n.mean(),mwu_p=stats.mannwhitneyu(a,n).pvalue)
res['rural_vs_nonrural']=rv
pd.DataFrame(rv).to_csv('out/rural_vs_nonrural.csv',index=False)
# multivariable OLS
X=['chr_pct_rural','acs_pct_black_alone','acs_pct_poverty','chr_pcp_per100k','chr_uninsured_pct_u65']
for yy in [y,'acs_hearing_pct']:
    d=m[[yy]+X].dropna(); Z=sm.add_constant(d[X]); fit=sm.OLS(d[yy],Z).fit(cov_type='HC3')
    vif={x:variance_inflation_factor(Z.values,i) for i,x in enumerate(Z.columns) if x!='const'}
    # standardized
    zs=(d-d.mean())/d.std(); fs=sm.OLS(zs[yy],sm.add_constant(zs[X])).fit(cov_type='HC3')
    res['ols_'+yy]=dict(n=int(fit.nobs),r2=fit.rsquared,adj_r2=fit.rsquared_adj,coef=fit.params.round(5).to_dict(),se_hc3=fit.bse.round(5).to_dict(),p=fit.pvalues.round(5).to_dict(),ci=fit.conf_int().round(5).values.tolist(),std_beta=fs.params.round(4).to_dict(),vif={k:round(v,2) for k,v in vif.items()})
# PLACES vs ACS agreement; internal correlation among predictors
d=m[['places_hearing_ageadj','acs_hearing_pct']].dropna(); res['places_vs_acs']=dict(zip(['rho','p'],stats.spearmanr(d.iloc[:,0],d.iloc[:,1])))
res['pred_corr']=m[X].corr(method='spearman').round(2).to_dict()
res['state_context']={'places_ageadj_range':[m[y].min(),m[y].max()],'acs_total_hearing_n':float(m.acs_hearing_n.sum()),'acs_total_pop':float(m.acs_civ_noninst_pop.sum()),
  'acs_state_pct':float(100*m.acs_hearing_n.sum()/m.acs_civ_noninst_pop.sum())}
d=m[m.chr_pcp_n>0][[y,'chr_pcp_per100k']]; r_=stats.spearmanr(d.iloc[:,1],d.iloc[:,0]); res['pcp_excl_zero_counties']=dict(n=len(d),rho=r_.statistic,p=r_.pvalue)
json.dump(res,open('out/results.json','w'),indent=1,default=float)
