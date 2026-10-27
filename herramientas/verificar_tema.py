"""Comprobaciones de integridad de un tema: notas, imágenes, viñetas anidadas, flechas y extensión.

Uso: python3 herramientas/verificar_tema.py "N. TEMA"
"""
import os
import re
import sys

carpeta = sys.argv[1]
md = os.path.join(carpeta, carpeta + '.md')
s = open(md, encoding='utf-8').read()
cuerpo, _, refs = s.partition('\n## Referencias')

usos = set(re.findall(r'\[\^([^\]]+)\](?!:)', cuerpo))
defs = set(re.findall(r'^\[\^([^\]]+)\]:', refs, re.M))
print('Notas sin definir:', sorted(usos - defs) or 'ninguna')
print('Notas sin usar:', sorted(defs - usos) or 'ninguna')

imgs = re.findall(r'\]\((assets/[^)]+)\)', s)
faltan = [i for i in imgs if not os.path.exists(os.path.join(carpeta, i))]
dir_assets = os.path.join(carpeta, 'assets')
sobran = set()
if os.path.isdir(dir_assets):
    sobran = {'assets/' + f for f in os.listdir(dir_assets)} - set(imgs)
print('Imágenes usadas:', len(imgs), '| inexistentes:', faltan or 'ninguna', '| sin usar:', sorted(sobran) or 'ninguna')
print('Imágenes duplicadas:', sorted({i for i in imgs if imgs.count(i) > 1}) or 'ninguna')

anidadas = [n + 1 for n, l in enumerate(s.splitlines()) if re.match(r'^  +[-*] ', l)]
print('Viñetas anidadas (líneas):', anidadas or 'ninguna')
flechas = [n + 1 for n, l in enumerate(s.splitlines()) if re.search(r'→|->|⇒|←', l)]
print('Flechas (líneas):', flechas or 'ninguna')

secciones = set(re.findall(r'^#{2,3} (\d+(?:\.\d+)?)', s, re.M))
citadas = set(re.findall(r'secci[oó]n (\d+(?:\.\d+)?)', cuerpo))
for grupo in re.findall(r'secciones ((?:\d+(?:\.\d+)?(?:, | y | a )?)+)', cuerpo):
    citadas |= set(re.findall(r'\d+(?:\.\d+)?', grupo))
print('Remisiones a secciones inexistentes:', sorted(citadas - secciones) or 'ninguna')
tablas = re.findall(r'\*\*Tabla (\d+)\.', s)
print('Tablas numeradas:', tablas)
remitidas = set(re.findall(r'\btablas? (\d+)', s))
print('Remisiones a tablas inexistentes:', sorted(remitidas - set(tablas), key=int) or 'ninguna')
figuras = sorted(set(re.findall(r'\(figura \d+', s, re.I)))
print('Remisiones a figuras numeradas (la compilación no numera figuras):', figuras or 'ninguna')
print('Palabras del cuerpo:', len(re.sub(r'\[\^[^\]]+\]', '', cuerpo).split()))
