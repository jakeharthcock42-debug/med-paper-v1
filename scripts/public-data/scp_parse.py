import pandas as pd, io, re, glob, sys
def parse(path):
    lines=open(path,encoding='utf-8',errors='ignore').read().split('\n')
    i=[k for k,l in enumerate(lines) if l.startswith('County,FIPS')][0]
    title=' | '.join(l.strip().strip('"') for l in lines[:i] if l.strip())
    body=[]
    for l in lines[i:]:
        if not l.strip(): break
        body.append(l)
    df=pd.read_csv(io.StringIO('\n'.join(body)),dtype=str)
    return title,df
