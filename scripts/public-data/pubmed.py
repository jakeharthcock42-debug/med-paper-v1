import sys,requests,json
def s(q,n=8):
    r=requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',params={'db':'pubmed','term':q,'retmode':'json','retmax':n,'sort':'relevance'}).json()['esearchresult']
    ids=r['idlist']; print(f"\n## {q}  [count={r['count']}]")
    if not ids: return
    d=requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi',params={'db':'pubmed','id':','.join(ids),'retmode':'json'}).json()['result']
    for i in ids:
        x=d[i]; print(i,x['pubdate'][:4],x['source'],'|',x['title'][:130],'|',x['authors'][0]['name'] if x['authors'] else '')
for q in sys.argv[1:]: s(q)
