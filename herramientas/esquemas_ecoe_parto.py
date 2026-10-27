"""Esquema de la guía práctica ECOE de trabajo de parto.

Uso: python3 herramientas/esquemas_ecoe_parto.py "<carpeta assets>"
- ecoe_tp_schultze_duncan.png: corte esquemático del útero después del nacimiento con los dos
  mecanismos de desprendimiento de la placenta. Schultze: el desprendimiento empieza en el centro,
  con un hematoma retroplacentario central, y la placenta sale invertida como un paraguas, con la cara
  fetal por delante y el sangrado después. Duncan: el desprendimiento empieza por un borde, la sangre
  sale antes que la placenta y esta se expulsa por el borde, con la cara materna por delante.
  No reproduce un caso real.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

OUT = sys.argv[1]
INK = "#0b0b0b"
SURF = "#fcfcfb"
PARED = "#e2bdb7"
PARED_BORDE = "#a8857f"
CAVIDAD = "#fbf3f1"
PLACENTA = "#8f5a6a"
SANGRE = "#b5485a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})

A_IN, B_IN = 2.6, 3.4   # cavidad
A_OUT, B_OUT = 3.6, 4.5  # pared


def elipse(a, b, t):
    return np.column_stack([a * np.cos(t), b * np.sin(t)])


def utero(ax):
    t = np.linspace(np.radians(-80), np.radians(260), 300)
    ext = elipse(A_OUT, B_OUT, t)
    ext = np.vstack([[0.9, -6.2], ext, [-0.9, -6.2]])
    ax.add_patch(Polygon(ext, closed=True, facecolor=PARED, edgecolor=PARED_BORDE, linewidth=1.2))
    cav = elipse(A_IN, B_IN, np.linspace(np.radians(-80), np.radians(260), 300))
    cav = np.vstack([[0.3, -6.2], cav, [-0.3, -6.2]])
    ax.add_patch(Polygon(cav, closed=True, facecolor=CAVIDAD, edgecolor=PARED_BORDE, linewidth=1.0))


def placenta(ax, desp, hematoma):
    th = np.radians(np.linspace(35, 145, 120))
    pared = elipse(A_IN, B_IN, th)
    # Normal hacia dentro de la elipse de la cavidad.
    dir_ = -np.column_stack([pared[:, 0] / A_IN ** 2, pared[:, 1] / B_IN ** 2])
    dir_ /= np.linalg.norm(dir_, axis=1)[:, None]
    externa = pared + dir_ * desp(th)[:, None]
    interna = externa + dir_ * 0.75
    ax.add_patch(Polygon(np.vstack([externa, interna[::-1]]), closed=True, facecolor=PLACENTA,
                         edgecolor="#5e3542", linewidth=1.0, zorder=4))
    if hematoma:
        ax.add_patch(Polygon(np.vstack([pared, externa[::-1]]), closed=True, facecolor=SANGRE,
                             edgecolor="none", zorder=3))
    return pared, externa


def schultze(ax):
    utero(ax)
    placenta(ax, lambda th: 1.1 * np.sin((th - th[0]) / (th[-1] - th[0]) * np.pi), True)
    ax.text(0, -0.6, "Hematoma\nretroplacentario\ncentral", ha="center", va="top", fontsize=15, color=INK)
    ax.set_title("Schultze (más frecuente)", fontsize=17, fontweight="bold", color=INK, pad=8)
    ax.text(0, -6.6, "Sale primero la cara fetal;\nel sangrado aparece después", ha="center", va="top",
            fontsize=15, color=INK)


def duncan(ax):
    utero(ax)
    pared, externa = placenta(ax, lambda th: np.clip((np.radians(75) - th) / np.radians(40), 0, 1) * 1.2,
                              False)
    # Sangre que escurre por la pared derecha hacia el cuello antes de la expulsión.
    t = np.radians(np.linspace(35, -80, 80))
    via = elipse(A_IN - 0.18, B_IN - 0.18, t)
    via = np.vstack([via, [[0.12, -6.1]]])
    ax.plot(via[:, 0], via[:, 1], color=SANGRE, linewidth=6, solid_capstyle="round", zorder=3)
    ax.text(-0.4, -0.6, "Desprendimiento\npor el borde", ha="center", va="top", fontsize=15, color=INK)
    ax.set_title("Duncan", fontsize=17, fontweight="bold", color=INK, pad=8)
    ax.text(0, -6.6, "Sangrado antes de la expulsión;\nsale primero la cara materna", ha="center", va="top",
            fontsize=15, color=INK)


def esquema():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 6.6))
    for ax, f in zip(axs, (schultze, duncan)):
        f(ax)
        ax.set_xlim(-4.8, 4.8)
        ax.set_ylim(-8.4, 5.0)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.subplots_adjust(wspace=0.05)
    fig.savefig(os.path.join(OUT, "ecoe_tp_schultze_duncan.png"), dpi=200, bbox_inches="tight",
                pad_inches=0.1)
    plt.close(fig)


os.makedirs(OUT, exist_ok=True)
esquema()
