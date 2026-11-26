import pandas as pd, numpy as np
from scipy import stats
import statsmodels.api as sm
def load():
    m=pd.read_csv('master_county_ms.csv',dtype={'fips':str})
    return m
def scp():
    return pd.read_csv('scp_all_long.csv',dtype={'fips':str})
def county_scp(ds,s=None):
    s=scp() if s is None else s
    d=s[(s.dataset==ds)&(~s.fips.isin(['28000','00000']))].copy()
    return d
def state_row(ds,s=None,fips='28000'):
    s=scp() if s is None else s
    d=s[(s.dataset==ds)&(s.fips==fips)]
    return d.iloc[0]
def se_from_ci(lo,hi): return (np.log(hi)-np.log(lo))/(2*1.96)
def rr(r1,lo1,hi1,r2,lo2,hi2):
    se=np.sqrt(se_from_ci(lo1,hi1)**2+se_from_ci(lo2,hi2)**2)
    est=r1/r2; return est, est*np.exp(-1.96*se), est*np.exp(1.96*se)
def spearman(x,y):
    d=pd.concat([x,y],axis=1).dropna()
    if len(d)<10: return (len(d),np.nan,np.nan)
    r,p=stats.spearmanr(d.iloc[:,0],d.iloc[:,1]); return len(d),r,p
def ols(df,y,xs,label=''):
    d=df[[y]+xs].dropna()
    X=sm.add_constant(d[xs]); mod=sm.OLS(d[y],X).fit(cov_type='HC3')
    t=pd.DataFrame({'coef':mod.params,'se':mod.bse,'p':mod.pvalues,'ci_lo':mod.conf_int()[0],'ci_hi':mod.conf_int()[1]})
    return mod,t,len(d)
def mdtable(df,floatfmt=3):
    return df.to_markdown(floatfmt=f'.{floatfmt}f') if hasattr(df,'to_markdown') else str(df)
