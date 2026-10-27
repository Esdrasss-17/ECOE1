"""Esquema de la guía práctica ECOE de cervicovaginitis en el embarazo.

Uso: python3 herramientas/esquemas_ecoe_cv.py "<carpeta assets>"
- ecoe_cv_linea_tiempo.png: línea de tiempo del embarazo del caso de la rúbrica (FUM 1 de junio de
  2023, consulta a las 22 semanas y 5 días, fecha probable de parto a los 280 días), con los
  periodos de las tres ecografías de la NOM-007 y del cribado de diabetes gestacional (24 a 28
  semanas). No reproduce un caso real.
"""
import os
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = sys.argv[1]
INK = "#0b0b0b"
INK2 = "#52514e"
SURF = "#fcfcfb"
TRIM = ["#f3ece9", "#efe6e2", "#ebe0db"]
ECO = "#5b7fa6"
CTG = "#b07a2a"
MARCA = "#b5485a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})


def esquema():
    fig, ax = plt.subplots(figsize=(10.0, 4.4))
    for i, (a, b, t) in enumerate([(0, 14, "Primer trimestre"), (14, 28, "Segundo trimestre"),
                                   (28, 42, "Tercer trimestre")]):
        ax.add_patch(Rectangle((a, 0), b - a, 1.0, facecolor=TRIM[i], edgecolor="none"))
        ax.text((a + b) / 2 if i != 1 else 18.3, 0.5, t, ha="center", va="center", fontsize=15, color=INK2)
    # Ecografías de la NOM-007 y cribado de diabetes gestacional.
    for a, b, t in [(11, 13 + 6 / 7, "11 a 13,6"), (18, 22, "18 a 22"), (29, 34, "29 a 30 o más")]:
        ax.add_patch(Rectangle((a, 1.25), b - a, 0.5, facecolor=ECO, edgecolor="none", alpha=0.9))
        ax.text((a + b) / 2, 1.95, t, ha="center", va="bottom", fontsize=15, color=INK)
    ax.text(0.2, 1.5, "Ecografías", ha="left", va="center", fontsize=15, color=ECO, fontweight="bold")
    ax.add_patch(Rectangle((24, -0.75), 4, 0.5, facecolor=CTG, edgecolor="none", alpha=0.9))
    ax.text(26, -0.95, "Cribado de diabetes\ngestacional, 24 a 28", ha="center", va="top", fontsize=15,
            color=INK)
    # Marcas del caso.
    for x, arriba, abajo in [(0, "FUM", "1 jun 2023"), (22 + 5 / 7, "Consulta", "22 sem 5 d\n7 nov 2023"),
                             (40, "FPP", "7 mar 2024")]:
        ax.plot([x, x], [-0.15, 1.15], color=MARCA, linewidth=2.4)
        ax.text(x, 2.75, arriba, ha="center", va="bottom", fontsize=15, color=MARCA, fontweight="bold")
        ax.plot([x, x], [1.15, 2.7], color=MARCA, linewidth=1.0, linestyle=(0, (2, 2)))
        if x != 22 + 5 / 7:
            ax.text(x, -0.3, abajo, ha="center", va="top", fontsize=15, color=INK)
    ax.text(22 + 5 / 7, 3.25, "22 sem 5 d · 7 nov 2023", ha="center", va="bottom", fontsize=15, color=INK)
    for s in range(0, 43, 4):
        ax.text(s, -2.15, str(s), ha="center", va="top", fontsize=13, color=INK2)
    ax.text(21, -2.75, "Semanas de gestación", ha="center", va="top", fontsize=15, color=INK2)
    ax.plot([0, 42], [-2.0, -2.0], color=INK2, linewidth=0.8)
    ax.set_xlim(-1.5, 43.5)
    ax.set_ylim(-3.3, 3.9)
    ax.axis("off")
    fig.savefig(os.path.join(OUT, "ecoe_cv_linea_tiempo.png"), dpi=200, bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


os.makedirs(OUT, exist_ok=True)
esquema()
