"""Añade un botón pequeño "Índice" en la esquina superior derecha de cada página del PDF,
que enlaza con la página del índice, y conserva los marcadores.

Uso: python3 herramientas/boton_indice.py archivo.pdf
"""
import os
import sys
import pymupdf

ruta = sys.argv[1]
doc = pymupdf.open(ruta)
indice = next(i for i in range(min(6, doc.page_count))
              if doc[i].get_text().lstrip().startswith('Índice'))
for i, pag in enumerate(doc):
    if i == indice:
        continue
    w = pag.rect.width
    r = pymupdf.Rect(w - 72, 20, w - 30, 34)
    pag.draw_rect(r, color=(0.12, 0.31, 0.47), fill=(0.93, 0.95, 0.98), width=0.6, radius=0.25)
    ancho = pymupdf.get_text_length('Índice', fontname='helv', fontsize=7.5)
    pag.insert_text((r.x0 + (r.width - ancho) / 2, r.y1 - 4.2), 'Índice', fontsize=7.5,
                    fontname='helv', color=(0.12, 0.31, 0.47))
    pag.insert_link({'kind': pymupdf.LINK_GOTO, 'from': r, 'page': indice,
                     'to': pymupdf.Point(0, 0)})
tmp = ruta + '.tmp'
doc.save(tmp, garbage=3, deflate=True)
doc.close()
os.replace(tmp, ruta)
d = pymupdf.open(ruta)
print('índice en la página', indice + 1, '| marcadores', len(d.get_toc()))
