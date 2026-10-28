"""Esquema de la guía práctica ECOE de hemorragia obstétrica, aborto y RCTG.

Uso: python3 herramientas/esquemas_ecoe_hemorragia.py "<carpeta assets>"
- ecoe_hem_mapa_sangrado.png: franja temporal del embarazo y el puerperio con las causas de sangrado de
  cada periodo (antes de las 22 semanas, desde las 22 semanas hasta el nacimiento y después del
  nacimiento) y, debajo, las herramientas comunes a los tres periodos. Se construye solo con las
  clasificaciones de las fuentes de los temas 6, 7 y 2; no reproduce un caso real.
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
C1 = "#e9d8e4"
C2 = "#f2dcc8"
C3 = "#dbe6ef"
BORDE = "#8a8984"
COMUN = "#eeeeea"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})


def caja(ax, x, y, w, h, color, titulo, lineas):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.18",
                                facecolor=color, edgecolor=BORDE, linewidth=1.2))
    ax.text(x + w / 2, y + h - 0.35, titulo, ha="center", va="top", fontsize=16, fontweight="bold",
            color=INK)
    ax.text(x + 0.3, y + h - 1.15, "\n".join(lineas), ha="left", va="top", fontsize=15, color=INK,
            linespacing=1.45)


def esquema():
    fig, ax = plt.subplots(figsize=(14.5, 8.4))
    w, h, y = 4.55, 4.55, 3.15
    caja(ax, 0.0, y, w, h, C1, "Antes de las 22 semanas",
         ["Aborto: amenaza, inevitable,", "incompleto, completo,", "diferido y séptico",
          "Embarazo ectópico", "Enfermedad trofoblástica"])
    caja(ax, w + 0.25, y, w, h, C2, "De las 22 semanas al parto",
         ["Placenta previa (sin dolor)", "Desprendimiento (dolor,", "útero hipertónico)",
          "Ruptura uterina (cicatriz)", "Vasa previa (sangrado fetal)"])
    caja(ax, 2 * (w + 0.25), y, w, h, C3, "Después del nacimiento",
         ["Las 4 T:", "Tono (atonía, la causa", "más frecuente)", "Trauma (desgarros, ruptura,",
          "inversión)", "Tejido (restos, acretismo)", "Trombina (coagulopatía)"])
    # Flecha del tiempo.
    ax.annotate("", xy=(14.35, y + h + 0.45), xytext=(0.0, y + h + 0.45),
                arrowprops=dict(arrowstyle="-|>", color=INK2, linewidth=2))
    ax.text(7.2, y + h + 0.65, "Edad gestacional", ha="center", va="bottom", fontsize=15, color=INK2)
    # Herramientas comunes.
    ax.add_patch(FancyBboxPatch((0.0, 0.0), 14.15, 2.75, boxstyle="round,pad=0.02,rounding_size=0.18",
                                facecolor=COMUN, edgecolor=BORDE, linewidth=1.2))
    ax.text(7.07, 2.5, "Común a los tres periodos", ha="center", va="top", fontsize=16,
            fontweight="bold", color=INK)
    ax.text(0.35, 1.8, "Madre: triage, índice de choque (normal hasta 0,9), Código Mater, reanimación del\n"
            "choque, biometría, grupo y Rh, coagulación con fibrinógeno y pruebas cruzadas\n"
            "Feto (desde la viabilidad): frecuencia cardiaca fetal y registro cardiotocográfico",
            ha="left", va="top", fontsize=15, color=INK, linespacing=1.45)
    ax.set_xlim(-0.2, 14.5)
    ax.set_ylim(-0.2, y + h + 1.3)
    ax.axis("off")
    fig.savefig(os.path.join(OUT, "ecoe_hem_mapa_sangrado.png"), dpi=200, bbox_inches="tight",
                pad_inches=0.15)
    plt.close(fig)


os.makedirs(OUT, exist_ok=True)
esquema()
