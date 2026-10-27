"""Esquemas de la toma de citología cervical construidos a partir del Manual de Procedimientos
para la Toma de la Muestra de Citología Cervical (Secretaría de Salud).

Uso: python3 herramientas/esquemas_citologia.py "<carpeta assets>"
Sustituyen figuras del manual que se perdieron en la conversión y no reproducen imágenes reales:
- cc_esquema_espatula_ayre.png: espátula de Ayre modificada (extremo semicónico para el
  endocérvix, bifurcado para el exocérvix) y giros de 360° de la toma (figs. 21 y 22 del manual).
- cc_esquema_zona_transformacion.png: corte sagital del cuello con la zona de transformación
  en cuatro posiciones (fig. 25 del manual): negro, epitelio escamoso maduro; rayado, zona de
  transformación; punteado, epitelio endocervical original.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse, Circle

OUT = sys.argv[1]
INK = "#0b0b0b"
INK2 = "#52514e"
SURF = "#fcfcfb"
TEJIDO = "#ecd3cf"
TEJIDO_BORDE = "#a8857f"
ESPATULA = "#e6d3a8"
ESPATULA_BORDE = "#8a7350"
ESCAMOSO = "#2b2b2b"
ZT = "#b5485a"
CILINDRICO = "#5b7fa6"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 15,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "hatch.linewidth": 1.1,
})


# ---------------------------------------------------------------------------
# Esquema 1. Espátula de Ayre modificada y técnica de la toma.
# ---------------------------------------------------------------------------
def espatula(ax):
    # Mango plano; a la izquierda el extremo semicónico y a la derecha el bifurcado.
    ax.add_patch(Polygon([(-6.2, -0.28), (6.2, -0.28), (6.2, 0.28), (-6.2, 0.28)], closed=True,
                         facecolor=ESPATULA, edgecolor=ESPATULA_BORDE, linewidth=1))
    ax.add_patch(Polygon([(-6.2, -0.45), (-6.2, 0.45), (-7.4, 0.25), (-8.3, 0.0), (-7.4, -0.25)],
                         closed=True, facecolor=ESPATULA, edgecolor=ESPATULA_BORDE, linewidth=1))
    # Extremo bifurcado: una punta larga (se apoya en el orificio) y una corta (recorre el exocérvix).
    ax.add_patch(Polygon([(6.2, -0.6), (6.2, 0.6), (7.0, 0.6), (8.6, 0.25), (7.2, 0.12), (7.2, -0.1),
                          (7.6, -0.25), (7.6, -0.6)], closed=True,
                         facecolor=ESPATULA, edgecolor=ESPATULA_BORDE, linewidth=1))
    ax.annotate("Extremo semicónico\n(endocérvix)", xy=(-7.6, 0.05), xytext=(-7.6, 1.45),
                ha="center", va="bottom", fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.9))
    ax.annotate("Extremo bifurcado\n(exocérvix)", xy=(7.6, 0.2), xytext=(7.6, 1.45),
                ha="center", va="bottom", fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.9))
    ax.annotate("", xy=(-8.3, -1.0), xytext=(8.6, -1.0),
                arrowprops=dict(arrowstyle="<->", color=INK2, linewidth=1))
    ax.text(0.15, -1.2, "17,5 cm", ha="center", va="top", fontsize=15, color=INK)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-2.2, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")


def giro(ax, sentido, radio=1.45):
    # Flecha circular de 360° alrededor del orificio; "derecha" en sentido de las manecillas.
    t = np.linspace(0, 2 * np.pi * 0.9, 200)
    if sentido == "derecha":
        t = np.pi / 2 - t
    else:
        t = np.pi / 2 + t
    x, y = radio * np.cos(t), radio * np.sin(t)
    ax.plot(x[:-4], y[:-4], color=ZT, linewidth=1.8)
    ax.annotate("", xy=(x[-1], y[-1]), xytext=(x[-6], y[-6]),
                arrowprops=dict(arrowstyle="-|>", color=ZT, linewidth=1.8, mutation_scale=18))


def cervix_frontal(ax):
    ax.add_patch(Circle((0, 0), 1.15, facecolor=TEJIDO, edgecolor=TEJIDO_BORDE, linewidth=1))
    ax.add_patch(Ellipse((0, 0), 0.42, 0.2, facecolor=INK2, edgecolor=INK2))


def toma(ax, tipo):
    cervix_frontal(ax)
    if tipo == "exo":
        # Punta larga en el orificio y punta corta sobre el exocérvix.
        ax.plot([0, 1.0], [0, 0.0], color=ESPATULA_BORDE, linewidth=5, solid_capstyle="round")
        ax.plot([0.55, 1.0], [-0.22, -0.22], color=ESPATULA_BORDE, linewidth=5, solid_capstyle="round")
        giro(ax, "derecha")
        ax.set_title("Toma exocervical\ngiro de 360° a la derecha", fontsize=15, color=INK)
    else:
        ax.add_patch(Polygon([(-0.14, -0.1), (0.14, -0.1), (0, 0.12)], closed=True,
                             facecolor=ESPATULA_BORDE, edgecolor=ESPATULA_BORDE))
        giro(ax, "izquierda")
        ax.set_title("Toma endocervical\ngiro de 360° a la izquierda", fontsize=15, color=INK)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.9, 1.9)
    ax.set_aspect("equal")
    ax.axis("off")


def esquema_espatula():
    fig = plt.figure(figsize=(8.0, 5.0))
    ax0 = fig.add_axes([0.02, 0.55, 0.96, 0.45])
    espatula(ax0)
    ax1 = fig.add_axes([0.06, 0.0, 0.42, 0.45])
    ax2 = fig.add_axes([0.52, 0.0, 0.42, 0.45])
    toma(ax1, "exo")
    toma(ax2, "endo")
    fig.savefig(os.path.join(OUT, "cc_esquema_espatula_ayre.png"), dpi=200, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Esquema 2. Posición de la zona de transformación (corte sagital).
# ---------------------------------------------------------------------------
def trayecto():
    """Superficie del labio derecho: del fondo de saco al orificio externo y luego por el canal."""
    t = np.linspace(0, -np.pi / 2, 120)
    arco = np.column_stack([6 + 8 * np.cos(t), 14 + 14 * np.sin(t)])
    recto = np.column_stack([np.linspace(6, 3.5, 20)[1:], np.zeros(19)])
    t2 = np.linspace(-np.pi / 2, -np.pi, 40)[1:]
    esquina = np.column_stack([3.5 + 2 * np.cos(t2), 2 + 2 * np.sin(t2)])
    canal = np.column_stack([np.full(80, 1.5), np.linspace(2, 30, 81)[1:]])
    p = np.vstack([arco, recto, esquina, canal])
    seg = np.hypot(*np.diff(p, axis=0).T)
    s = np.concatenate([[0], np.cumsum(seg)])
    s_os = s[len(arco) + len(recto) + len(esquina) - 1]
    return p, s_os - s  # distancia al orificio: positiva hacia el fondo de saco, negativa en el canal


def normales(p):
    d = np.gradient(p, axis=0)
    d /= np.hypot(d[:, 0], d[:, 1])[:, None]
    return np.column_stack([d[:, 1], -d[:, 0]])  # hacia el tejido


def banda(p, n, mascara, grosor):
    idx = np.where(mascara)[0]
    if len(idx) < 2:
        return None
    a, b = idx[0], idx[-1] + 1
    ext = p[a:b]
    inn = (p[a:b] + grosor * n[a:b])[::-1]
    return np.vstack([ext, inn])


def labio(ax, p, d, tramos, espejo):
    sx = -1 if espejo else 1
    q = p.copy()
    q[:, 0] *= sx
    contorno = np.vstack([q, [[sx * 14, 30]], [[sx * 14, 14]]])
    ax.add_patch(Polygon(contorno, closed=True, facecolor=TEJIDO, edgecolor=TEJIDO_BORDE, linewidth=1))
    n = normales(p)
    n[:, 0] *= sx
    estilos = {
        "escamoso": dict(facecolor=ESCAMOSO, edgecolor=ESCAMOSO, hatch=None),
        "zt": dict(facecolor="white", edgecolor=ZT, hatch="////"),
        "cilindrico": dict(facecolor="white", edgecolor=CILINDRICO, hatch=".."),
    }
    for tipo, (d1, d2) in tramos.items():
        poli = banda(q, n, (d >= d1) & (d <= d2), 2.0)
        if poli is not None:
            ax.add_patch(Polygon(poli, closed=True, linewidth=0.8, **estilos[tipo]))


def panel(ax, titulo, tramos):
    p, d = trayecto()
    for espejo in (False, True):
        labio(ax, p, d, tramos, espejo)
    ax.set_title(titulo, fontsize=15.5, color=INK, pad=6)
    ax.set_xlim(-16, 16)
    ax.set_ylim(-3, 31)
    ax.set_aspect("equal")
    ax.axis("off")


def esquema_zona():
    fig = plt.figure(figsize=(8.6, 5.0))
    largo = 40  # cualquier distancia mayor que la longitud del trayecto
    paneles = [
        ("A. Zona de\ntransformación",
         {"escamoso": (3, largo), "zt": (-1, 3), "cilindrico": (-largo, -1)}),
        ("B. Evertida",
         {"escamoso": (9, largo), "zt": (5, 9), "cilindrico": (-largo, 5)}),
        ("C. Ampliamente\nevertida",
         {"escamoso": (16, largo), "zt": (11, 16), "cilindrico": (-largo, 11)}),
        ("D. Retraída\n(posmenopausia o\npostratamiento)",
         {"escamoso": (-4, largo), "zt": (-9, -4), "cilindrico": (-largo, -9)}),
    ]
    for i, (titulo, tramos) in enumerate(paneles):
        ax = fig.add_axes([0.01 + i * 0.247, 0.2, 0.235, 0.66])
        panel(ax, titulo, tramos)
    leyenda = fig.add_axes([0.0, 0.1, 1.0, 0.12])
    leyenda.axis("off")
    leyenda.set_xlim(0, 100)
    leyenda.set_ylim(0, 10)
    items = [("Escamoso maduro", dict(facecolor=ESCAMOSO, edgecolor=ESCAMOSO)),
             ("Zona de transformación", dict(facecolor="white", edgecolor=ZT, hatch="////")),
             ("Endocervical original", dict(facecolor="white", edgecolor=CILINDRICO, hatch=".."))]
    for x, (texto, estilo) in zip((2, 32, 68), items):
        leyenda.add_patch(Polygon([(x, 3), (x + 4, 3), (x + 4, 7), (x, 7)], closed=True, linewidth=0.8, **estilo))
        leyenda.text(x + 5.2, 5, texto, va="center", fontsize=15, color=INK)
    fig.savefig(os.path.join(OUT, "cc_esquema_zona_transformacion.png"), dpi=200, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


os.makedirs(OUT, exist_ok=True)
esquema_espatula()
esquema_zona()
print("esquemas generados en", OUT)
