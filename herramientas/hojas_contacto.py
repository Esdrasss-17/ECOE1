"""Genera hojas de contacto de las páginas de un PDF para revisarlas visualmente.

Uso: python3 herramientas/hojas_contacto.py archivo.pdf carpeta_salida [resolución]
"""
import glob
import os
import subprocess
import sys

from PIL import Image

pdf, salida = sys.argv[1], sys.argv[2]
res = sys.argv[3] if len(sys.argv) > 3 else '50'
os.makedirs(salida, exist_ok=True)
for f in glob.glob(os.path.join(salida, '*.png')):
    os.remove(f)
subprocess.run(['pdftoppm', '-r', res, '-png', pdf, os.path.join(salida, 'p')], check=True)
paginas = sorted(glob.glob(os.path.join(salida, 'p-*.png')))
for k in range(0, len(paginas), 12):
    ims = [Image.open(f) for f in paginas[k:k + 12]]
    w, h = ims[0].size
    hoja = Image.new('RGB', (w * 6, h * 2), 'white')
    for i, im in enumerate(ims):
        hoja.paste(im, ((i % 6) * w, (i // 6) * h))
    hoja.save(os.path.join(salida, f'hoja{k // 12}.png'))
print(len(paginas), 'páginas')
