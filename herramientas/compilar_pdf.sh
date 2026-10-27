#!/usr/bin/env bash
# Uso: herramientas/compilar_pdf.sh "<carpeta del tema>" "<título para el pie>" ["<nombre del .md>"]
# Con ENLACES=1 añade índice, enlaces internos, marcadores y botón de índice en cada página.
# Genera <carpeta>/<nombre>.pdf a partir de <carpeta>/<nombre>.md; sin tercer argumento, <nombre> es el de la carpeta.
set -euo pipefail
export LANG=C.UTF-8 LC_ALL=C.UTF-8
H="$(cd "$(dirname "$0")" && pwd)"; D="$(cd "$1" && pwd)"; N="${3:-$(basename "$D")}"; N="${N%.md}"; TMP="$(mktemp -d)"
python3 "$H/preparar_md.py" "$D/$N.md" "$TMP/build.md"
pandoc "$TMP/build.md" -f markdown -t html5 --standalone --embed-resources --css "$H/estilo.css" -o "$TMP/doc.html"
python3 "$H/postprocesar_html.py" "$TMP/doc.html"
if [ "${ENLACES:-0}" = 1 ]; then python3 "$H/enlaces_html.py" "$TMP/doc.html"; fi
NODE_PATH="$(npm root -g)" node "$H/html_a_pdf.js" "$TMP/doc.html" "$D/$N.pdf" "$2"
if [ "${ENLACES:-0}" = 1 ]; then python3 "$H/boton_indice.py" "$D/$N.pdf"; fi
python3 -c "import pymupdf,sys;d=pymupdf.open(sys.argv[1]);print(d.page_count,'páginas',sum(len(p.get_images()) for p in d),'imágenes')" "$D/$N.pdf"
