"""Esquema de la guía práctica ECOE de enfermedades hipertensivas del embarazo y diabetes gestacional.

Uso: python3 herramientas/esquemas_ecoe_ehe.py "<carpeta assets>"
- ecoe_ehe_magnesio_escala.png: escala vertical de la concentración sérica de magnesio con el rango
  terapéutico (4 a 8 mEq/L) y los efectos que aparecen al aumentar la concentración: pérdida de los
  reflejos osteotendinosos (alrededor de 7), depresión respiratoria (alrededor de 10) y paro cardiaco
  (alrededor de 25). Se construye solo con esas cifras; no reproduce un caso real.
"""
import os
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = sys.argv[1]
INK = "#0b0b0b"
INK2 = "#52514e"
SURF = "#fcfcfb"
EJE = "#a3a29d"
TERAP = "#d9ead3"
TERAP_BORDE = "#6a9a5b"
ALERTA = "#b5485a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})


def y(v):
    # Escala comprimida por encima de 12 mEq/L para que quepa el paro cardiaco (25).
    return v if v <= 12 else 12 + (v - 12) * 0.35


def esquema():
    fig, ax = plt.subplots(figsize=(9.0, 7.6))
    x0 = 1.0
    ax.plot([x0, x0], [0, y(27)], color=EJE, linewidth=3, solid_capstyle="round")
    for v in (0, 2, 4, 6, 8, 10, 12, 25):
        ax.plot([x0 - 0.12, x0], [y(v), y(v)], color=EJE, linewidth=2)
        ax.text(x0 - 0.22, y(v), str(v), ha="right", va="center", fontsize=15, color=INK2)
    # Corte de escala entre 12 y 25.
    ax.text(x0 + 0.02, y(18), "≈", ha="center", va="center", fontsize=22, color=EJE,
            bbox=dict(boxstyle="square,pad=0.05", facecolor=SURF, edgecolor="none"))
    ax.text(x0 - 0.55, y(27) + 0.4, "mEq/L", ha="center", va="bottom", fontsize=15, color=INK2)

    ax.add_patch(FancyBboxPatch((x0 + 0.25, 4), 1.2, 4, boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=TERAP, edgecolor=TERAP_BORDE, linewidth=1.4))
    ax.text(x0 + 1.65, 4.9, "Rango terapéutico: 4 a 8 mEq/L\n(meta de la GPC: 5 a 7 mEq/L)", ha="left",
            va="center", fontsize=15, color=INK)

    eventos = [(7, "Pérdida de los reflejos osteotendinosos (primer signo)"),
               (10, "Depresión respiratoria"),
               (25, "Paro cardiaco")]
    for v, txt in eventos:
        ax.plot([x0, x0 + 1.45], [y(v), y(v)], color=ALERTA, linewidth=2.4)
        ax.plot([x0], [y(v)], marker="o", markersize=10, color=ALERTA)
        dy = 0.3 if v == 7 else 0
        ax.text(x0 + 1.65, y(v) + dy, txt, ha="left", va="center", fontsize=15, color=INK)

    ax.text(x0 + 1.65, -1.6, "Antídoto: gluconato de calcio al 10%, 10 mL (1 g) IV en 3 minutos",
            ha="left", va="center", fontsize=15, color=INK)
    ax.set_xlim(-0.2, 8.6)
    ax.set_ylim(-2.4, y(27) + 1.4)
    ax.axis("off")
    fig.savefig(os.path.join(OUT, "ecoe_ehe_magnesio_escala.png"), dpi=200, bbox_inches="tight",
                pad_inches=0.15)
    plt.close(fig)


os.makedirs(OUT, exist_ok=True)
esquema()
