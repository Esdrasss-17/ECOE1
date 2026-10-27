"""Navegación interna del HTML antes de convertirlo en PDF; no cambia el texto.

Uso: python3 herramientas/enlaces_html.py doc.html
- Índice con enlaces a las secciones numeradas (h2 y h3), antes de la sección 1.
- Enlaces en las menciones "sección N", "secciones N y M", "Tabla N" y en la columna
  "Sección" de las tablas.
- Cada referencia de la bibliografía enlaza de vuelta a su primera cita.
"""
import re
import sys

p = sys.argv[1]
h = open(p, encoding='utf-8').read()

# Secciones numeradas: número -> id.
sec = {}
items = []
for m in re.finditer(r'<h([23]) id="([^"]+)"[^>]*>(\d+(?:\.\d+)?)\.?\s+([^<]*)</h\1>', h):
    nivel, ident, num, titulo = m.groups()
    titulo = ' '.join(titulo.split())
    sec[num] = ident
    items.append((nivel, ident, num, titulo))
for m in re.finditer(r'<h2 id="([^"]+)"[^>]*>((?:Anexo|Referencias)[^<]*)</h2>', h):
    items.append(('2', m.group(1), '', m.group(2)))

# Tablas: id en el título.
def tabla(m):
    return f'<p class="tcap" id="tabla-{m.group(1)}"><strong>Tabla {m.group(1)}.'
h = re.sub(r'<p class="tcap"><strong>Tabla (\d+)\.', tabla, h)
tablas = set(re.findall(r'id="tabla-(\d+)"', h))

# Índice.
filas = []
for nivel, ident, num, titulo in items:
    sangria = ' class="toc3"' if nivel == '3' else ''
    filas.append(f'<li{sangria}><a href="#{ident}">{(num + " ") if num else ""}{titulo}</a></li>')
indice = ('<nav id="indice"><p class="toc-titulo"><strong>Índice</strong></p><ul class="toc">'
          + ''.join(filas) + '</ul></nav>')
primero = re.search(r'<h2 id="[^"]+"[^>]*>1\. ', h)
h = h[:primero.start()] + indice + h[primero.start():]


def enlazar_num(num):
    return f'<a class="int" href="#{sec[num]}">{num}</a>' if num in sec else num


def en_texto(fragmento):
    def secciones(m):
        nums = re.sub(r'\d+(?:\.\d+)?', lambda n: enlazar_num(n.group(0)), m.group(2))
        return m.group(1) + nums
    fragmento = re.sub(r'(secci(?:ón|ones) )((?:\d+(?:\.\d+)?)(?:(?:, | y | a )\d+(?:\.\d+)?)*)',
                       secciones, fragmento)
    fragmento = re.sub(r'\b(Tablas? )(\d+)\b(?!\.\d)',
                       lambda m: (f'{m.group(1)}<a class="int" href="#tabla-{m.group(2)}">{m.group(2)}</a>'
                                  if m.group(2) in tablas else m.group(0)), fragmento)
    return fragmento


# Solo texto fuera de etiquetas, encabezados, títulos de tabla y enlaces existentes.
partes = re.split(r'(<h[1-6][^>]*>.*?</h[1-6]>|<p class="tcap".*?</p>|<a [^>]*>.*?</a>|<[^>]+>)', h,
                  flags=re.S)
h = ''.join(x if (x.startswith('<')) else en_texto(x) for x in partes)

# Columna "Sección" (última columna) de la Tabla 1.
m1 = re.search(r'id="tabla-1".*?(<table.*?</table>)', h, flags=re.S)
if m1:
    t = re.sub(r'<td>([\d. y]+)</td>(\s*</tr>)',
               lambda m: '<td>' + re.sub(r'\d+(?:\.\d+)?', lambda n: enlazar_num(n.group(0)), m.group(1))
               + '</td>' + m.group(2), m1.group(1))
    h = h[:m1.start(1)] + t + h[m1.end(1):]

# Citas: id en la primera aparición y regreso desde la bibliografía.
vistos = set()
def cita(m):
    n = m.group(1)
    if n in vistos:
        return m.group(0)
    vistos.add(n)
    return f'<a id="cita-{n}" href="#ref-{n}">'
h = re.sub(r'<a href="#ref-(\d+)">', cita, h)
h = re.sub(r'<span id="ref-(\d+)"></span>',
           lambda m: m.group(0) + (f'<a class="volver" href="#cita-{m.group(1)}">[cita]</a> '
                                   if m.group(1) in vistos else ''), h)

estilo = ('<style>nav#indice{break-before:page;page-break-before:always;break-after:page;page-break-after:always}'
          'ul.toc{list-style:none;padding-left:0;margin:4px 0;font-size:10.5pt;line-height:1.45}'
          'ul.toc li.toc3{padding-left:18px;font-size:9.75pt}'
          'ul.toc a,a.int,a.volver{color:#1f4e79;text-decoration:none}'
          'a.volver{font-size:8pt}</style>')
h = h.replace('</head>', estilo + '</head>', 1)
open(p, 'w', encoding='utf-8').write(h)
print('secciones', len(sec), 'tablas', len(tablas), 'citas', len(vistos),
      'enlaces internos', h.count('class="int"'))
