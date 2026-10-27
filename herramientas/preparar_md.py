import re,sys,os
src,out=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf-8').read()
defs={m.group(1):m.group(2).strip() for m in re.finditer(r'^\[\^([A-Za-z0-9]+)\]:\s*(.+)$',s,re.M)}
body=re.sub(r'^\[\^([A-Za-z0-9]+)\]:.*\n?','',s,flags=re.M)
order=[]
for k in re.findall(r'\[\^([A-Za-z0-9]+)\]',body):
    if k not in order: order.append(k)
num={k:i+1 for i,k in enumerate(order)}
def grp(m):
    ks=re.findall(r'\[\^([A-Za-z0-9]+)\]',m.group(0))
    ns=sorted({num[k] for k in ks})
    return '<sup>'+','.join(f'<a href="#ref-{n}">{n}</a>' for n in ns)+'</sup>'
body=re.sub(r'(?:\[\^[A-Za-z0-9]+\])+',grp,body)
body=body.rstrip()+'\n\n'+'\n'.join(f'{num[k]}. <span id="ref-{num[k]}"></span>{defs[k]}' for k in order)+'\n'
body=re.sub(r'\]\(assets/',']('+os.path.dirname(os.path.abspath(src))+'/assets/',body)
open(out,'w',encoding='utf-8').write(body)
