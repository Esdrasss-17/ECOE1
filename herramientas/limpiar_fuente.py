"""Reduce un .md convertido de PDF a texto útil para lectura.
Uso: python3 limpiar_fuente.py <fuente.md> <salida.txt>
Elimina bloques OCR duplicados (<details>, texto de imagen con <br>), cabeceras de impresión de UpToDate,
números de página aislados y listas de referencias bibliográficas largas."""
import re, sys
s = open(sys.argv[1], encoding='utf-8').read()
s = re.sub(r'<details>.*?</details>', '', s, flags=re.S)
s = re.sub(r'<!-- Start of picture text -->.*?<!-- End of picture text -->', '', s, flags=re.S)
out = []; skip = False
for l in s.splitlines():
    t = l.strip()
    if re.match(r'^#+\s*\**\s*(REFERENCES|Referencias|Bibliografía|BIBLIOGRAFÍA|7\.\s*Bibliograf|Bibliography)\b', t, re.I):
        skip = True; continue
    if skip and re.match(r'^(#+ |## Documento|---)', t): skip = False
    if skip: continue
    if 'uptodate.com/contents' in t or re.fullmatch(r'\d+/\d+', t) or re.fullmatch(r'\*?\*?\d{1,3}\*?\*?', t): continue
    if re.match(r'^\d+/\d+/\d+, \d+:\d+ [ap]\. ?m\.', t): continue
    if '<br>' in t and not t.startswith('|'): continue
    out.append(l)
s = '\n'.join(out)
s = re.sub(r'\n{3,}', '\n\n', s)
open(sys.argv[2], 'w', encoding='utf-8').write(s)
print(len(s)//1024, 'KB')
