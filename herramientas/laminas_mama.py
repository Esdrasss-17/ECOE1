"""Compone las láminas de autoexploración y exploración clínica del tema 10 a partir de las figuras de la GPC S-001-08.

Uso: python3 herramientas/laminas_mama.py <carpeta de imágenes extraídas> <carpeta assets>
Recorta cada figura con su pie impreso (sin las franjas de texto de la página) y las agrupa en filas.
"""
import sys
import numpy as np
from PIL import Image
P = sys.argv[1] + '/GPC_Ca_mama_en_el_primer_nivel.pdf-'
OUT = sys.argv[2]

def recorte(n, box=None):
    im = Image.open(P + n + '.png').convert('RGB')
    if box: im = im.crop(box)
    a = np.array(im.convert('L')) < 200
    ys, xs = np.where(a)
    return im.crop((max(xs.min() - 6, 0), max(ys.min() - 6, 0), min(xs.max() + 7, im.width), min(ys.max() + 7, im.height)))

def fila(ims, alto, gap=30):
    ims = [i.resize((round(i.width * alto / i.height), alto), Image.LANCZOS) for i in ims]
    W = sum(i.width for i in ims) + gap * (len(ims) - 1)
    c = Image.new('RGB', (W, alto), 'white'); x = 0
    for i in ims: c.paste(i, (x, 0)); x += i.width + gap
    return c

def columna(filas, gap=30):
    W = max(f.width for f in filas); H = sum(f.height for f in filas) + gap * (len(filas) - 1)
    c = Image.new('RGB', (W, H), 'white'); y = 0
    for f in filas: c.paste(f, ((W - f.width) // 2, y)); y += f.height + gap
    return c

def guardar(im, nombre):
    b = Image.new('RGB', (im.width + 40, im.height + 40), 'white'); b.paste(im, (20, 20))
    b.save(f'{OUT}/{nombre}.png'); print(nombre, b.size)

f1, f2, f3, f4, f5 = (recorte(n) for n in ['0044-15', '0044-16', '0044-17', '0044-18', '0045-02'])
guardar(columna([fila([f1, f2, f3], 300), fila([f4, f5], 300)]), 'cm_autoexploracion_gpc')
f11 = recorte('0048-02', (300, 85, 1070, 490))
f12 = recorte('0048-10', (0, 58, 1034, 432))
guardar(fila([f11, f12], 420), 'cm_exploracion_inspeccion_axila_gpc')
guardar(recorte('0049-02', (0, 88, 1059, 356)), 'cm_exploracion_supraclavicular_gpc')
f14 = recorte('0049-03', (0, 217, 1062, 442))
f17 = recorte('0050-03', (0, 574, 1059, 856))
guardar(fila([f14, f17], 300), 'cm_exploracion_palpacion_pezon_gpc')
guardar(recorte('0049-04', (0, 64, 1059, 384)), 'cm_exploracion_cuadrantes_externos_gpc')
