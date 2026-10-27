"""Esquemas de la inserción placentaria construidos a partir de las definiciones de la GPC IMSS-589-19.

Uso: python3 herramientas/esquemas_placenta.py "<carpeta assets>"
No reproducen imágenes reales:
- pl_esquema_previa.png: relación del borde placentario con el orificio cervical interno
  (normal a 20 mm o más, inserción baja a menos de 20 mm sin cubrirlo, previa sobre el orificio).
- pl_esquema_acretismo.png: profundidad de las vellosidades en la pared uterina
  (acreta sin penetrar el miometrio, increta dentro del miometrio, percreta a través de la serosa).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

OUT = sys.argv[1]
INK = "#0b0b0b"
INK2 = "#52514e"
SURF = "#fcfcfb"
PARED = "#d9c7bd"
PARED_BORDE = "#9c857a"
PLACENTA = "#b5485a"
DECIDUA = "#e9d9a6"
SEROSA = "#7a6a62"
VEJIGA = "#bcd3e6"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 8.5,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
})

A, B, GROSOR = 60.0, 75.0, 12.0  # semiejes de la cavidad y grosor de la pared (mm aproximados)
CERVIX_LARGO, CERVIX_ANCHO = 32.0, 22.0


def contorno(angulos, ra, rb):
    return np.column_stack([ra * np.cos(angulos), rb * np.sin(angulos)])


def banda(t1, t2, ra, rb, ancho):
    t = np.linspace(t1, t2, 120)
    externo = contorno(t, ra, rb)
    interno = contorno(t[::-1], ra - ancho, rb - ancho)
    return np.vstack([externo, interno])


def utero(ax):
    # Pared uterina sin el sector inferior, donde se abre el canal cervical.
    hueco = np.arcsin(CERVIX_ANCHO / 2 / (A + GROSOR)) * 0.55
    t1, t2 = -np.pi / 2 + hueco, 3 * np.pi / 2 - hueco
    ax.add_patch(Polygon(banda(t1, t2, A + GROSOR, B + GROSOR, GROSOR), closed=True,
                         facecolor=PARED, edgecolor=PARED_BORDE, linewidth=0.8))
    # Cuello uterino con su canal.
    y0 = -(B + GROSOR) + 3
    ax.add_patch(Rectangle((-CERVIX_ANCHO / 2, y0 - CERVIX_LARGO), CERVIX_ANCHO, CERVIX_LARGO,
                           facecolor=PARED, edgecolor=PARED_BORDE, linewidth=0.8))
    ax.plot([0, 0], [y0 - CERVIX_LARGO, -B], color=PARED_BORDE, linewidth=1.4)
    ax.plot(0, -B, marker="o", markersize=4, color=INK)
    ax.text(-CERVIX_ANCHO / 2 - 2, -B - 9, "OCI", ha="right", va="center", fontsize=8, color=INK)
    ax.text(0, y0 - CERVIX_LARGO - 3, "Cuello uterino", ha="center", va="top", fontsize=7.5, color=INK2)


def placenta(ax, t_inferior, t_superior):
    ax.add_patch(Polygon(banda(t_inferior, t_superior, A, B, 14), closed=True,
                         facecolor=PLACENTA, edgecolor="#7d2a3a", linewidth=0.6, alpha=0.92))


def cota(ax, punto, texto):
    ax.plot([punto[0], 0], [punto[1], -B], color=INK, linewidth=0.9, linestyle=(0, (3, 2)))
    medio = (punto[0] / 2, (punto[1] - B) / 2)
    ax.text(medio[0] - 3, medio[1] + 5, texto, ha="right", va="bottom", fontsize=8.5,
            color=INK, fontweight="bold")


def esquema_previa():
    fig, ejes = plt.subplots(1, 3, figsize=(7.4, 3.6))
    casos = [
        ("Inserción normal", "Borde a 20 mm o más del OCI", np.deg2rad(-35), np.deg2rad(70), "≥ 20 mm"),
        ("Inserción baja", "Borde a menos de 20 mm, sin cubrir el OCI", np.deg2rad(-78), np.deg2rad(40), "< 20 mm"),
        ("Placenta previa", "El tejido placentario cubre el OCI", np.deg2rad(-130), np.deg2rad(10), None),
    ]
    for ax, (titulo, sub, t_inf, t_sup, etiqueta) in zip(ejes, casos):
        utero(ax)
        placenta(ax, t_inf, t_sup)
        if etiqueta:
            borde = contorno(np.array([t_inf]), A - 7, B - 7)[0]
            cota(ax, borde, etiqueta)
        ax.set_title(titulo, fontsize=9.5, fontweight="bold", color=INK, pad=4)
        ax.text(0, B + GROSOR + 8, sub, ha="center", va="bottom", fontsize=7.4, color=INK2, wrap=True)
        ax.set_xlim(-A - GROSOR - 6, A + GROSOR + 6)
        ax.set_ylim(-B - GROSOR - CERVIX_LARGO - 12, B + GROSOR + 22)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.tight_layout(w_pad=0.6)
    fig.savefig(os.path.join(OUT, "pl_esquema_previa.png"), dpi=220)
    plt.close(fig)


def vellosidad(ax, x, base, fondo, ancho=3.2):
    puntos = [(x - ancho / 2, base), (x - ancho / 3, (base + fondo) / 2), (x, fondo),
              (x + ancho / 3, (base + fondo) / 2), (x + ancho / 2, base)]
    ax.add_patch(Polygon(puntos, closed=True, facecolor="#7d2a3a", edgecolor="#5e1f2b", linewidth=0.5))


def esquema_acretismo():
    # Capas de arriba hacia abajo: placenta, decidua basal, miometrio, serosa, vejiga.
    y_placenta, y_decidua, y_miometrio, y_serosa, y_vejiga = 100, 88, 82, 40, 37
    fig, ejes = plt.subplots(1, 4, figsize=(7.4, 3.5))
    casos = [
        ("Inserción normal", "Vellosidades ancladas\nen la decidua", True, y_decidua - 3, False),
        ("Acreta", "Adheridas al miometrio,\nsin penetrarlo", False, y_miometrio, False),
        ("Increta", "Invaden el\nmiometrio", False, 56, False),
        ("Percreta", "Atraviesan la serosa\nhasta órganos vecinos", False, 26, True),
    ]
    for ax, (titulo, sub, con_decidua, fondo, vejiga) in zip(ejes, casos):
        ax.add_patch(Rectangle((0, y_vejiga - 22), 40, 22, facecolor=VEJIGA, edgecolor="#8aa9c2", linewidth=0.6))
        ax.add_patch(Rectangle((0, y_serosa), 40, y_miometrio - y_serosa, facecolor=PARED,
                               edgecolor=PARED_BORDE, linewidth=0.6))
        ax.add_patch(Rectangle((0, y_vejiga), 40, y_serosa - y_vejiga, facecolor=SEROSA, linewidth=0))
        if con_decidua:
            ax.add_patch(Rectangle((0, y_miometrio), 40, y_decidua - y_miometrio, facecolor=DECIDUA,
                                   edgecolor="#c9b678", linewidth=0.6))
            techo = y_decidua
        else:
            techo = y_miometrio
        ax.add_patch(Rectangle((0, techo), 40, y_placenta - techo, facecolor=PLACENTA,
                               edgecolor="#7d2a3a", linewidth=0.6, alpha=0.92))
        for x in (8, 20, 32):
            vellosidad(ax, x, techo + 7, fondo)
        ax.set_title(titulo, fontsize=9.5, fontweight="bold", color=INK, pad=4)
        ax.text(20, y_placenta + 3, sub, ha="center", va="bottom", fontsize=7.2, color=INK2,
                linespacing=1.15)
        ax.set_xlim(-1, 41)
        ax.set_ylim(y_vejiga - 24, y_placenta + 17)
        ax.axis("off")
    rotulos = [("Placenta", 94), ("Decidua basal", 85), ("Miometrio", 61), ("Serosa", 38.5), ("Vejiga", 25)]
    for texto, y in rotulos:
        ejes[0].text(-2, y, texto, ha="right", va="center", fontsize=7.4, color=INK2)
    fig.subplots_adjust(left=0.13, right=0.99, top=0.9, bottom=0.03, wspace=0.12)
    fig.savefig(os.path.join(OUT, "pl_esquema_acretismo.png"), dpi=220)
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    esquema_previa()
    esquema_acretismo()
