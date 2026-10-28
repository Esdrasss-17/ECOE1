"""Esquema de la guía práctica ECOE de cáncer de mama.

Uso: python3 herramientas/esquemas_ecoe_mama.py "<carpeta assets>"
- ecoe_cm_categorias_T.png: regla a escala de 0 a 66 mm con las categorías T del TNM por tamaño (T1mi,
  T1a, T1b, T1c, T2 y T3) y un recuadro con las subcategorías de T4, que no dependen del tamaño. Se construye solo con las definiciones del TNM que
  transcribe la GPC IMSS-232-09; no reproduce un caso real.
"""
import os
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

OUT = sys.argv[1]
INK = "#0b0b0b"
INK2 = "#52514e"
SURF = "#fcfcfb"
EJE = "#a3a29d"
TONOS = ["#f6e3ea", "#efcbd8", "#e6b0c4", "#db94af", "#c97a98", "#b5607f"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})


def esquema():
    fig, ax = plt.subplots(figsize=(14.5, 5.2))
    k = 0.22  # 1 mm = 0,22 unidades
    h = 1.5
    tramos = [(0, 1), (1, 5), (5, 10), (10, 20), (20, 50), (50, 66)]
    for (a, b), color in zip(tramos, TONOS):
        ax.add_patch(Rectangle((a * k, 0), (b - a) * k, h, facecolor=color, edgecolor=SURF, linewidth=2))
    for v in (0, 1, 5, 10, 20, 50):
        ax.plot([v * k, v * k], [-0.15, 0], color=INK2, linewidth=1.5)
    for v in (0, 5, 10, 20, 50):
        ax.text(v * k, -0.25, f"{v}", ha="center", va="top", fontsize=15, color=INK2)
    ax.text(66 * k, -0.25, "mm", ha="right", va="top", fontsize=15, color=INK2)
    # Categorías pequeñas: rótulo arriba con línea guía.
    for c, x, txt in [(0.5, 0.1, "T1mi: 1 mm o menos"), (3, 0.1, "T1a: más de 1 y hasta 5 mm"),
                      (7.5, 0.1, "T1b: más de 5 y hasta 10 mm")]:
        y = {0.5: 3.6, 3: 2.95, 7.5: 2.3}[c]
        ax.plot([c * k, c * k, x + 2.2], [h, y, y], color=EJE, linewidth=1.2)
        ax.text(x + 2.3, y, txt, ha="left", va="center", fontsize=15, color=INK)
    ax.text(15 * k, h / 2, "T1c\n>10 a 20", ha="center", va="center", fontsize=14, color=INK, linespacing=1.3)
    ax.text(35 * k, h / 2, "T2\nmás de 20 y hasta 50", ha="center", va="center", fontsize=15, color=INK,
            linespacing=1.3)
    ax.text(58 * k, h / 2, "T3\nmás de 50", ha="center", va="center", fontsize=14, color=SURF,
            fontweight="bold", linespacing=1.3)
    ax.text(0, -1.05, "Tamaño del tumor invasor, regla a escala", ha="left", va="top",
            fontsize=15, color=INK2)
    # T4.
    ax.add_patch(FancyBboxPatch((15.2, -0.2), 6.6, 4.1, boxstyle="round,pad=0.02,rounding_size=0.18",
                                facecolor="#eeeeea", edgecolor="#8a8984", linewidth=1.2))
    ax.text(18.5, 3.6, "T4: cualquier tamaño", ha="center", va="top", fontsize=16, fontweight="bold", color=INK)
    ax.text(15.5, 2.85, "T4a: pared torácica\nT4b: úlcera, nódulos satélite\no piel de naranja\n"
            "T4c: T4a y T4b\nT4d: carcinoma inflamatorio", ha="left", va="top", fontsize=15, color=INK,
            linespacing=1.45)
    ax.set_xlim(-0.3, 22.0)
    ax.set_ylim(-1.7, 4.1)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(os.path.join(OUT, "ecoe_cm_categorias_T.png"), dpi=200, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


os.makedirs(OUT, exist_ok=True)
esquema()
