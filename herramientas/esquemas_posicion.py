"""Esquema de las variedades de posición en la presentación de occipucio, construido con las definiciones de Williams (cap. 22).

Uso: python3 herramientas/esquemas_posicion.py "<carpeta assets>"
No reproduce un caso real. La pelvis se ve como la percibe el explorador desde el periné:
pubis arriba, sacro abajo y lado izquierdo materno (I) a la derecha del esquema;
D es el lado derecho materno. En cada cabeza,
la sutura sagital une la fontanela anterior (rombo) con la posterior (en "Y"), que señala el occipucio.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Polygon

OUT = sys.argv[1]
INK = "#0b0b0b"
INK2 = "#52514e"
SURF = "#fcfcfb"
PELVIS = "#e8dfd6"
PELVIS_BORDE = "#9c857a"
CABEZA = "#f2c9a8"
CABEZA_BORDE = "#b07a5a"
SUTURA = "#6b3f2a"
plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": SURF, "savefig.facecolor": SURF})

# Ángulo hacia donde apunta el occipucio en la vista del explorador (0° = derecha del esquema = izquierda materna).
VARIEDADES = [
    (0, 0, 90, "Occipitoanterior\ndirecta (OA)"),
    (0, 1, 45, "Occipitoanterior\nizquierda (LOA)"),
    (0, 2, 0, "Occipitotransversa\nizquierda (LOT)"),
    (0, 3, 315, "Occipitoposterior\nizquierda (LOP)"),
    (1, 0, 270, "Occipitoposterior\ndirecta (OP)"),
    (1, 1, 225, "Occipitoposterior\nderecha (ROP)"),
    (1, 2, 180, "Occipitotransversa\nderecha (ROT)"),
    (1, 3, 135, "Occipitoanterior\nderecha (ROA)"),
]


def punto(angulo, distancia):
    a = np.deg2rad(angulo)
    return np.array([np.cos(a), np.sin(a)]) * distancia


def cabeza(ax, angulo, r=0.55):
    ax.add_patch(Ellipse((0, 0), 2.3, 1.55, facecolor=PELVIS, edgecolor=PELVIS_BORDE, linewidth=1.0))
    ax.add_patch(Circle((0, 0), r, facecolor=CABEZA, edgecolor=CABEZA_BORDE, linewidth=1.0))
    occ = punto(angulo, 0.42 * r / 0.62)
    sin = punto(angulo, -0.42 * r / 0.62)
    ax.plot([occ[0], sin[0]], [occ[1], sin[1]], color=SUTURA, linewidth=1.6)
    # Fontanela posterior: dos suturas lambdoideas que se abren hacia el occipucio.
    for d in (-38, 38):
        extremo = occ + punto(angulo + d, 0.2)
        ax.plot([occ[0], extremo[0]], [occ[1], extremo[1]], color=SUTURA, linewidth=1.6)
    # Fontanela anterior: rombo con las suturas coronales hacia los lados.
    c = sin
    rombo = [c + punto(angulo, 0.09), c + punto(angulo + 90, 0.06), c + punto(angulo + 180, 0.09),
             c + punto(angulo - 90, 0.06)]
    ax.add_patch(Polygon(rombo, closed=True, facecolor=SUTURA, edgecolor=SUTURA))
    for d in (90, -90):
        extremo = c + punto(angulo + d, 0.24)
        ax.plot([c[0], extremo[0]], [c[1], extremo[1]], color=SUTURA, linewidth=1.3)


def rotulos(ax):
    ax.text(0, 0.86, "pubis", ha="center", va="center", fontsize=9.5, color=INK2)
    ax.text(0, -0.86, "sacro", ha="center", va="center", fontsize=9.5, color=INK2)
    ax.text(-1.2, 0, "D", ha="center", va="center", fontsize=9.5, color=INK2)
    ax.text(1.2, 0, "I", ha="center", va="center", fontsize=9.5, color=INK2)


def main():
    fig, ejes = plt.subplots(2, 4, figsize=(7.4, 4.1))
    for fila, col, angulo, rotulo in VARIEDADES:
        ax = ejes[fila][col]
        ax.set_xlim(-1.32, 1.32)
        ax.set_ylim(-1.05, 1.05)
        ax.set_aspect("equal")
        ax.axis("off")
        cabeza(ax, angulo)
        rotulos(ax)
        ax.set_title(rotulo, fontsize=12, color=INK, pad=1, linespacing=1.05)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.01, wspace=0.06, hspace=0.38)
    fig.savefig(os.path.join(OUT, "tp_esquema_variedades_posicion.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    main()
