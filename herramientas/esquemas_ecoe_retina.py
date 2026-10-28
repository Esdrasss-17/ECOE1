"""Esquema de la guía práctica ECOE de retinopatías.

Uso: python3 herramientas/esquemas_ecoe_retina.py "<carpeta assets>"
- ecoe_rd_edema_macular_grados.png: tres paneles del polo posterior de un ojo derecho (papila a la
  derecha, en el lado nasal) con los grados del edema macular de la escala clínica internacional:
  leve (engrosamiento o exudados duros en el polo posterior, distantes del centro de la mácula),
  moderado (próximos al centro sin afectarlo) y severo (afectan el centro). Se construye solo con
  esas definiciones; no reproduce un caso real.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse

OUT = sys.argv[1]
INK = "#0b0b0b"
SURF = "#fcfcfb"
FONDO = "#e9b7a1"
PAPILA = "#f6dfc6"
ARTERIA = "#c0503f"
VENA = "#8e2f2b"
EDEMA = "#d99a7c"
EXUDADO = "#f2d34f"
EXUDADO_BORDE = "#a8892a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})

PX, PY = 2.6, 0.0     # papila (lado nasal, a la derecha en el ojo derecho)
FX, FY = -1.6, -0.25  # centro de la fóvea


def arcada(ax, signo, color, ancho, desplaz):
    t = np.linspace(0, 1, 200)
    x = PX - 0.2 - t * 6.2
    y = signo * (0.25 + desplaz + 2.4 * np.sin(np.pi * np.clip(t * 0.85, 0, 1)) ** 0.8)
    ax.plot(x, y, color=color, linewidth=ancho, solid_capstyle="round", zorder=2)


def fondo(ax):
    ax.add_patch(Circle((0, 0), 4.6, facecolor=FONDO, edgecolor="#b98470", linewidth=1.2, zorder=0))
    for s in (1, -1):
        arcada(ax, s, VENA, 3.2, 0.25)
        arcada(ax, s, ARTERIA, 2.2, 0.0)
    ax.add_patch(Ellipse((PX, PY), 1.0, 1.15, facecolor=PAPILA, edgecolor="#d9b48f", linewidth=1.2, zorder=3))
    # Región macular (círculo de trazos) y centro de la fóvea.
    ax.add_patch(Circle((FX, FY), 1.25, facecolor="none", edgecolor=INK, linewidth=1.2,
                        linestyle=(0, (4, 3)), zorder=4))
    ax.add_patch(Circle((FX, FY), 0.12, facecolor=INK, edgecolor="none", zorder=6))


def lesion(ax, cx, cy, r):
    ax.add_patch(Circle((cx, cy), r, facecolor=EDEMA, edgecolor="none", alpha=0.85, zorder=3))
    rng = np.random.default_rng(int(abs(cx * 10 + cy * 7)) + 3)
    for _ in range(9):
        a = rng.uniform(0, 2 * np.pi)
        d = rng.uniform(0.15, r * 0.85)
        ax.add_patch(Circle((cx + d * np.cos(a), cy + d * np.sin(a)), rng.uniform(0.07, 0.13),
                            facecolor=EXUDADO, edgecolor=EXUDADO_BORDE, linewidth=0.6, zorder=5))


def panel(ax, titulo, cx, cy, r, texto):
    fondo(ax)
    lesion(ax, cx, cy, r)
    ax.set_title(titulo, fontsize=17, fontweight="bold", color=INK, pad=6)
    ax.text(0, -5.1, texto, ha="center", va="top", fontsize=15, color=INK)
    ax.set_xlim(-4.9, 4.9)
    ax.set_ylim(-7.0, 5.0)
    ax.set_aspect("equal")
    ax.axis("off")


def esquema():
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 6.2))
    panel(axs[0], "Leve", 0.7, 1.25, 0.7, "Polo posterior,\nlejos del centro")
    panel(axs[1], "Moderado", -1.6, 1.05, 0.6, "Cerca del centro,\nsin afectarlo")
    panel(axs[2], "Severo", FX, FY, 0.85, "Afecta el centro\nde la mácula")
    # Leyenda común en una fila propia, con los elementos separados.
    ley = fig.add_axes([0.08, 0.0, 0.84, 0.07])
    ley.set_xlim(0, 40)
    ley.set_ylim(-1, 1)
    ley.axis("off")
    ley.add_patch(Ellipse((0.6, 0), 0.5, 0.9, facecolor=EXUDADO, edgecolor=EXUDADO_BORDE))
    ley.text(1.3, 0, "Exudados duros", va="center", fontsize=15, color=INK)
    ley.add_patch(Ellipse((10.9, 0), 0.9, 1.6, facecolor=EDEMA, edgecolor="none"))
    ley.text(11.8, 0, "Engrosamiento", va="center", fontsize=15, color=INK)
    ley.add_patch(Ellipse((21.0, 0), 0.4, 0.75, facecolor=INK, edgecolor="none"))
    ley.text(21.6, 0, "Centro de la mácula", va="center", fontsize=15, color=INK)
    ley.plot([31.0, 32.6], [0, 0], color=INK, linewidth=1.2, linestyle=(0, (4, 3)))
    ley.text(33.0, 0, "Región macular", va="center", fontsize=15, color=INK)
    fig.subplots_adjust(wspace=0.04, bottom=0.12)
    fig.savefig(os.path.join(OUT, "ecoe_rd_edema_macular_grados.png"), dpi=200, bbox_inches="tight",
                pad_inches=0.15)
    plt.close(fig)


os.makedirs(OUT, exist_ok=True)
esquema()
