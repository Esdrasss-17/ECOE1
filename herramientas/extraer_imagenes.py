"""Extrae las imágenes del PDF de imágenes seleccionadas de un tema con su nombre original.
Uso: python3 extraer_imagenes.py "<N. TEMA.pdf>" <carpeta_salida>
Cada página del PDF contiene una imagen; el índice (TOC) guarda el nombre de archivo original."""
import sys, os, pymupdf as fitz
d = fitz.open(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
for lvl, title, p in d.get_toc():
    name = title.split(' — ')[-1]; page = d[p-1]; imgs = page.get_images(full=True)
    if not imgs: continue
    pix = fitz.Pixmap(d, imgs[0][0])
    if pix.alpha: pix = fitz.Pixmap(pix, 0)
    if pix.n - pix.alpha > 3: pix = fitz.Pixmap(fitz.csRGB, pix)
    pix.save(os.path.join(out, name))
print(len(os.listdir(out)), 'imágenes en', out)
