import re,sys
p=sys.argv[1]; h=open(p,encoding='utf-8').read()
h=re.sub(r'<p><strong>(Tabla [^<]*)</strong>',r'<p class="tcap"><strong>\1</strong>',h)
def tab(m):
    t=m.group(0); return t.replace('<table>','<table class="keep">',1) if t.count('<tr')<=14 else t
h=re.sub(r'<table>.*?</table>',tab,h,flags=re.S)
h=re.sub(r'<figure>(\s*<img[^>]*>\s*<figcaption[^>]*>Foto estándar)',r'<figure class="half">\1',h)
open(p,'w',encoding='utf-8').write(h)
print('captions',h.count('class="tcap"'),'keep',h.count('class="keep"'),'half',h.count('class="half"'))
