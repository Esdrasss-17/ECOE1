"""Convierte una guía ECOE en Markdown a un guion de texto para síntesis de voz.

Uso: python3 md_a_audio.py guia.md salida.txt
Quita notas, imágenes, formato y referencias; lee la tabla de la rúbrica como frases;
desarrolla siglas y unidades. Separa los capítulos con una línea '=== título'.
"""
import re
import sys

src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
s = re.sub(r'^---\n.*?\n---\n', '', s, flags=re.S)
s = s.split('\n## Referencias')[0]

MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto',
         'septiembre', 'octubre', 'noviembre', 'diciembre']

SIGLAS = [
    (r'\bAHF, APNP y APP\b', 'antecedentes heredofamiliares, personales no patológicos y personales patológicos'),
    (r'\bAHF\b', 'antecedentes heredofamiliares'), (r'\bAPNP\b', 'antecedentes personales no patológicos'),
    (r'\bAPP\b', 'antecedentes personales patológicos'), (r'\bAGO\b', 'antecedentes ginecoobstétricos'),
    (r'\bIVSA\b', 'inicio de la vida sexual'), (r'\bMPF\b', 'método de planificación familiar'),
    (r'\bFUM\b', 'fecha de última menstruación'), (r'\bFPP\b', 'fecha probable de parto'),
    (r'\bSDG\b', 'semanas de gestación'), (r'\blas ITS\b', 'las infecciones de transmisión sexual'),
    (r'\buna ITS\b', 'una infección de transmisión sexual'), (r'\bITS\b', 'infecciones de transmisión sexual'),
    (r'\bla VB\b', 'la vaginosis bacteriana'), (r'\bVB\b', 'vaginosis bacteriana'),
    (r'\bla CVV\b', 'la candidosis vulvovaginal'), (r'\bCVV\b', 'candidosis vulvovaginal'),
    (r'\bKOH\b', 'hidróxido de potasio'), (r'\bNAAT\b', 'prueba de amplificación de ácidos nucleicos'),
    (r'\bVIH\b', 've i hache'), (r'\bVPH\b', 'virus del papiloma humano'),
    (r'\buna RPM\b', 'una rotura prematura de membranas'), (r'\bla RPM\b', 'la rotura prematura de membranas'),
    (r'\bRPM\b', 'rotura prematura de membranas'), (r'\bGPC\b', 'guía de práctica clínica'),
    (r'\bIMSS\b', 'i eme ese ese'), (r'\bVDRL\b', 've de erre ele'), (r'\bCDC\b', 'ce de ce'),
    (r'\bOMS\b', 'o eme ese'), (r'\bUI\b', 'unidades internacionales'), (r'\bECOE\b', 'ecoe'),
    (r'\bNOM-(\d)(\d)(\d)(-[A-Z0-9-]+)?', lambda m: 'norma oficial ' + ' '.join(
        ['cero' if d == '0' else d for d in m.group(1, 2, 3)])),
    (r'\bpH\b', 'pe hache'),
]
UNIDADES = [
    (r'(\d)\s?mmHg', r'\1 milímetros de mercurio'), (r'(\d)\s?°C', r'\1 grados'),
    (r'(\d)\s?mg\b', r'\1 miligramos'), (r'(\d)\s?mL\b', r'\1 mililitros'),
    (r'(\d)\s?kg\b', r'\1 kilos'), (r'(\d)\s?g\b', r'\1 gramos'), (r'(\d)\s?cm\b', r'\1 centímetros'),
    (r'(\d)\s?µg\b', r'\1 microgramos'), (r'(\d)\s?%', r'\1 por ciento'),
    (r'(\d+)/(\d+) milímetros', r'\1 sobre \2 milímetros'),
    (r'/dL\b', ' por decilitro'), (r'(\d) m\b', r'\1 metros'), (r'\bRh\b', 'erre hache'),
    (r'(\d) lpm\b', r'\1 latidos por minuto'),
]


def fecha(m):
    d, mes, a = int(m.group(1)), int(m.group(2)), m.group(3)
    return f'{d} de {MESES[mes - 1]} de {a}'


def limpiar(t):
    t = re.sub(r'\[\^[^\]]+\]', '', t)
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?', '', t)
    t = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t)
    t = t.replace('**', '').replace('`', '')
    t = re.sub(r'(?<!\w)\*([^*\n]+)\*(?!\w)', r'\1', t)
    t = re.sub(r'(\d{2})/(\d{2})/(\d{4})', fecha, t)
    t = re.sub(r'(\d+)\.(\d) semanas de gestación', r'\1 semanas y \2 días', t)
    t = re.sub(r'(\d+)\.(\d) SDG', r'\1 semanas y \2 días', t)
    for a, b in SIGLAS:
        t = re.sub(a, b, t)
    for a, b in UNIDADES:
        t = re.sub(a, b, t)
    t = re.sub(r' ?\((secci[oó]n|secciones) [\d., ya]+\)', '', t)
    t = re.sub(r'(\d+),(\d) semanas', r'\1 semanas y \2 días', t)
    t = re.sub(r'\b(\d+)\.(\d+)\b', r'\1 punto \2', t)
    t = t.replace(' · ', '. ').replace('"', '').replace('“', '').replace('”', '')
    t = re.sub(r'[ \t]+', ' ', t).replace(' .', '.').replace(' ,', ',').replace(' :', ':')
    return t.strip()


lineas, tabla, salida = s.splitlines(), [], []
for l in lineas:
    if l.startswith('|'):
        tabla.append(l)
        continue
    if tabla:
        filas = [r for r in tabla[2:]]
        for r in filas:
            c = [x.strip() for x in r.strip('|').split('|')]
            salida.append(limpiar(f'Criterio {c[0]}. {c[1]}. Se espera: {c[2]}.'))
        tabla = []
    if l.startswith('**Siglas de uso frecuente') or l.strip() == '---':
        continue
    if l.startswith('**Tabla'):
        salida.append('Los criterios de la rúbrica son los siguientes.')
        continue
    h = re.match(r'^(#{1,3}) (.*)', l)
    if h:
        titulo = limpiar(h.group(2))
        titulo = re.sub(r'^(\d+)\.(\d+) ', r'Apartado \1 punto \2. ', titulo)
        titulo = re.sub(r'^(\d+)\. ', r'Sección \1. ', titulo)
        salida.append(('=== ' if len(h.group(1)) <= 2 else '') + titulo + '.')
        continue
    l = re.sub(r'^\s*[-*] ', '', l)
    l = re.sub(r'^\s*(\d+)\. ', r'\1. ', l)
    t = limpiar(l)
    if t:
        if not re.search(r'[.:;?!]$', t):
            t += '.'
        salida.append(t)

open(out, 'w', encoding='utf-8').write('\n'.join(salida) + '\n')
print(len(' '.join(salida).split()), 'palabras')
