"""Sintetiza un guion de audio (de guia_a_guion_audio.py) en un MP3 con capítulos.

Uso: python3 herramientas/guion_a_mp3.py guion.txt voz.onnx salida.mp3 "Título"
Cada línea '=== título' abre un capítulo. Requiere piper-tts y ffmpeg con libmp3lame.
La voz usada para la guía de cervicovaginitis es es-mls_10246-low (Piper v0.0.2).
"""
import os
import subprocess
import sys
import tempfile
import wave

guion, voz, salida, titulo = sys.argv[1:5]
capitulos, actual = [], None
for linea in open(guion, encoding='utf-8'):
    linea = linea.strip()
    if not linea:
        continue
    if linea.startswith('=== '):
        actual = [linea[4:].rstrip('.'), [linea[4:]]]
        capitulos.append(actual)
    elif actual:
        actual[1].append(linea)

tmp = tempfile.mkdtemp()
wavs, marcas, t = [], [], 0.0
for i, (nombre, lineas) in enumerate(capitulos):
    w = os.path.join(tmp, f'{i:02d}.wav')
    subprocess.run([sys.executable, '-m', 'piper', '-m', voz, '-f', w, '--sentence-silence', '0.35'],
                   input='\n'.join(lineas), text=True, check=True, capture_output=True)
    with wave.open(w) as f:
        dur = f.getnframes() / f.getframerate() + 1.5
    marcas.append((nombre, t, t + dur))
    t += dur
    wavs.append(w)
    print(f'{nombre}: {dur / 60:.1f} min', flush=True)

lista = os.path.join(tmp, 'lista.txt')
silencio = os.path.join(tmp, 'silencio.wav')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=16000:cl=mono',
                '-t', '1.5', '-c:a', 'pcm_s16le', silencio], check=True)
with open(lista, 'w') as f:
    for w in wavs:
        f.write(f"file '{w}'\nfile '{silencio}'\n")
meta = os.path.join(tmp, 'meta.txt')
with open(meta, 'w', encoding='utf-8') as f:
    f.write(f';FFMETADATA1\ntitle={titulo}\nartist=Guías ECOE\n')
    for nombre, a, b in marcas:
        f.write(f'[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(a * 1000)}\nEND={int(b * 1000)}\ntitle={nombre}\n')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lista, '-i', meta,
                '-map_metadata', '1', '-map_chapters', '1', '-ac', '1', '-c:a', 'libmp3lame', '-b:a', '56k',
                '-id3v2_version', '3', salida], check=True)
print(f'Total: {t / 60:.1f} min')
