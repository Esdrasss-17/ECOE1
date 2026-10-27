"""Esquemas de la guía práctica ECOE de cáncer cervicouterino.

Uso: python3 herramientas/esquemas_ecoe_cacu.py "<carpeta assets>"
No reproducen imágenes reales; se construyen solo con las definiciones citadas en la guía:
- ecoe_cacu_triple_toma.png: corte sagital esquemático de la vagina y el cuello con los tres
  sitios de la triple toma en su orden (fondo de saco vaginal posterior, exocérvix, endocérvix).
- ecoe_cacu_estadios_figo2018.png: ocho paneles con la extensión que define cada etapa de la
  FIGO 2018 (IB, IIA, IIB, IIIA, IIIB, IIIC, IVA, IVB). La etapa IA es microscópica y no se dibuja.
"""
import os
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse, Circle, FancyBboxPatch

OUT = sys.argv[1]
INK = "#0b0b0b"
INK2 = "#52514e"
SURF = "#fcfcfb"
TEJIDO = "#ecd3cf"
TEJIDO_BORDE = "#a8857f"
CUELLO = "#e2bdb7"
LUZ = "#ffffff"
TUMOR = "#b5485a"
PARED = "#a3a29d"
GANGLIO = "#f3ece9"
VASO = "#7f93ad"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 15,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
})


# ---------------------------------------------------------------------------
# Esquema 1. Triple toma (corte sagital; introito a la izquierda, útero a la derecha).
# ---------------------------------------------------------------------------
def marca(ax, x, y, n):
    ax.add_patch(Circle((x, y), 0.36, facecolor=TUMOR, edgecolor="white", linewidth=1.5, zorder=6))
    ax.text(x, y - 0.02, str(n), ha="center", va="center", fontsize=15, color="white",
            fontweight="bold", zorder=7)


def esquema_triple_toma():
    fig, ax = plt.subplots(figsize=(9.0, 4.6))
    ax.add_patch(Polygon([(-0.6, -3.4), (13.9, -3.4), (13.9, 3.4), (-0.6, 3.4)], closed=True,
                         facecolor=TEJIDO, edgecolor="none"))
    # Luz vaginal alrededor del cuello: el fondo de saco posterior es más profundo que el anterior.
    luz = [(0, 0.75), (6.4, 1.45), (8.0, 1.85), (8.55, 1.55), (8.1, 1.12), (7.25, 0.95),
           (6.95, 0.45), (6.95, -0.45), (7.25, -0.95), (8.2, -1.15), (9.2, -1.55), (9.55, -2.05),
           (8.8, -2.35), (6.4, -1.65), (0, -0.75)]
    ax.add_patch(Polygon(luz, closed=True, facecolor=LUZ, edgecolor=TEJIDO_BORDE, linewidth=1.2))
    cuello = [(11.2, 1.3), (8.55, 1.32), (8.1, 1.12), (7.25, 0.95), (6.95, 0.45), (6.95, -0.45),
              (7.25, -0.95), (8.2, -1.15), (9.2, -1.42), (11.2, -1.4)]
    ax.add_patch(Polygon(cuello, closed=True, facecolor=CUELLO, edgecolor=TEJIDO_BORDE, linewidth=1.2))
    ax.add_patch(Polygon([(6.95, 0.1), (11.2, 0.13), (11.2, -0.13), (6.95, -0.1)], closed=True,
                         facecolor=LUZ, edgecolor=TEJIDO_BORDE, linewidth=0.9))
    ax.text(3.2, 0.0, "Vagina", ha="center", va="center", fontsize=15, color=INK)
    ax.text(-0.35, -1.05, "Introito", ha="left", va="top", fontsize=15, color=INK)
    ax.text(12.1, 0.0, "Útero", ha="center", va="center", fontsize=15, color=INK, rotation=90)
    ax.annotate("Fondo de saco anterior", xy=(8.25, 1.65), xytext=(9.3, 2.75), ha="center",
                va="bottom", fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.9))
    ax.annotate("Orificio cervical externo", xy=(6.95, 0.0), xytext=(3.4, 2.75), ha="center",
                va="bottom", fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.9))
    ax.annotate("Exocérvix", xy=(7.05, -0.65), xytext=(5.0, -1.0), ha="center", va="center",
                fontsize=15, color=INK, arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.9))
    ax.annotate("Fondo de saco posterior", xy=(9.15, -2.0), xytext=(5.6, -3.25), ha="center",
                va="bottom", fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.9))
    ax.annotate("Conducto endocervical", xy=(10.5, -0.05), xytext=(11.3, -3.25), ha="center",
                va="bottom", fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.9))
    marca(ax, 8.85, -1.75, 1)
    marca(ax, 7.55, 0.62, 2)
    marca(ax, 9.2, 0.0, 3)
    ax.set_xlim(-0.7, 14.0)
    ax.set_ylim(-3.5, 3.6)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(os.path.join(OUT, "ecoe_cacu_triple_toma.png"), dpi=200, bbox_inches="tight",
                pad_inches=0.1)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Esquema 2. Etapas FIGO 2018 (corte coronal salvo IVA, que es sagital, e IVB).
# ---------------------------------------------------------------------------
def pelvis(ax, ureteres=True):
    for x in (-4.6, 4.2):
        ax.add_patch(Polygon([(x, -3.6), (x + 0.4, -3.6), (x + 0.4, 3.0), (x, 3.0)], closed=True,
                             facecolor=PARED, edgecolor="none"))
    for s in (-1, 1):
        ax.add_patch(Polygon([(s * 0.85, 0.35), (s * 4.15 if s > 0 else -4.15, 0.6),
                              (s * 4.15 if s > 0 else -4.15, 1.75), (s * 0.85, 1.9)], closed=True,
                             facecolor="#f4e6e3", edgecolor=TEJIDO_BORDE, linewidth=0.6,
                             linestyle=(0, (2, 2))))
    ax.add_patch(Ellipse((0, 3.7), 3.4, 3.6, facecolor=TEJIDO, edgecolor=TEJIDO_BORDE, linewidth=1))
    ax.add_patch(Polygon([(-0.85, 2.15), (0.85, 2.15), (0.85, 0.25), (-0.85, 0.25)], closed=True,
                         facecolor=CUELLO, edgecolor=TEJIDO_BORDE, linewidth=1))
    ax.add_patch(Polygon([(-0.75, 0.25), (0.75, 0.25), (0.6, -3.6), (-0.6, -3.6)], closed=True,
                         facecolor=TEJIDO, edgecolor=TEJIDO_BORDE, linewidth=1))
    ax.plot([-0.7, 0.7], [-2.25, -2.25], color=INK2, linewidth=0.9, linestyle=(0, (3, 2)))
    if ureteres:
        for s in (-1, 1):
            ax.plot([s * 2.5, s * 1.9, s * 1.4], [5.9, 2.6, 0.8], color=VASO, linewidth=1.6)


def marco(ax, titulo, subtitulo):
    ax.text(0, 7.25, titulo, ha="center", va="bottom", fontsize=17, fontweight="bold", color=INK)
    ax.text(0, -4.0, subtitulo, ha="center", va="top", fontsize=15, color=INK, linespacing=1.15)
    ax.set_xlim(-5.0, 5.0)
    ax.set_ylim(-5.9, 8.1)
    ax.set_aspect("equal")
    ax.axis("off")


def tumor(ax, puntos):
    ax.add_patch(Polygon(puntos, closed=True, facecolor=TUMOR, edgecolor="#7d2a38", linewidth=1,
                         alpha=0.95, zorder=4))


def ganglio(ax, x, y, afectado):
    ax.add_patch(Ellipse((x, y), 0.62, 0.42, facecolor=TUMOR if afectado else GANGLIO,
                         edgecolor="#7d2a38" if afectado else TEJIDO_BORDE, linewidth=0.9, zorder=5))


def p_ib(ax):
    pelvis(ax)
    tumor(ax, [(-0.55, 1.9), (0.55, 1.9), (0.62, 0.6), (-0.62, 0.6)])
    marco(ax, "IB", "Limitado\nal cuello")


def p_iia(ax):
    pelvis(ax)
    tumor(ax, [(-0.6, 1.9), (0.6, 1.9), (0.66, 0.2), (0.66, -1.5), (-0.66, -1.5), (-0.66, 0.2)])
    ax.text(1.0, -1.0, "Vagina\nsuperior", ha="left", va="center", fontsize=15, color=INK)
    marco(ax, "IIA", "Dos tercios\nsuperiores de vagina")


def p_iib(ax):
    pelvis(ax)
    tumor(ax, [(0.6, 1.9), (-0.6, 1.9), (-2.7, 1.55), (-2.9, 1.1), (-2.6, 0.7), (-0.62, 0.5),
               (0.6, 0.5)])
    ax.text(-2.55, -0.3, "Parametrio", ha="center", va="center", fontsize=15, color=INK)
    marco(ax, "IIB", "Parametrio sin\nllegar a la pared")


def p_iiia(ax):
    pelvis(ax)
    tumor(ax, [(-0.6, 1.9), (0.6, 1.9), (0.66, 0.2), (0.6, -3.4), (-0.6, -3.4), (-0.66, 0.2)])
    ax.text(-0.9, -2.9, "Tercio\ninferior", ha="right", va="center", fontsize=15, color=INK)
    marco(ax, "IIIA", "Tercio inferior\nde vagina")


def p_iiib(ax):
    pelvis(ax, ureteres=False)
    ax.plot([2.5, 1.9, 1.4], [5.9, 2.6, 0.8], color=VASO, linewidth=1.6)
    ax.plot([-2.6, -2.05], [5.9, 2.0], color=VASO, linewidth=6.5, solid_capstyle="round")
    tumor(ax, [(0.6, 1.95), (-0.6, 1.95), (-4.15, 1.85), (-4.15, 0.45), (-0.62, 0.45), (0.6, 0.45)])
    ax.text(-2.15, 5.4, "Hidronefrosis", ha="center", va="bottom", fontsize=15, color=INK)
    marco(ax, "IIIB", "Pared pélvica o\nhidronefrosis")


def p_iiic(ax):
    pelvis(ax, ureteres=False)
    ax.plot([0, 0], [7.0, 5.7], color=VASO, linewidth=2.2)
    for s in (-1, 1):
        ax.plot([0, s * 1.9, s * 3.1], [5.7, 3.4, 0.6], color=VASO, linewidth=2.0)
    tumor(ax, [(-0.55, 1.9), (0.55, 1.9), (0.62, 0.6), (-0.62, 0.6)])
    for x, y in ((-2.05, 3.0), (2.05, 3.0), (-2.9, 1.2), (2.9, 1.2)):
        ganglio(ax, x, y, afectado=(x < 0))
    for y in (6.0, 6.75):
        ganglio(ax, 0.55, y, afectado=True)
    ax.text(-3.0, 0.1, "C1", ha="center", va="top", fontsize=15, color=INK, fontweight="bold")
    ax.text(1.05, 6.4, "C2", ha="left", va="center", fontsize=15, color=INK, fontweight="bold")
    marco(ax, "IIIC", "Ganglios pélvicos (C1)\no paraaórticos (C2)")


def p_iva(ax):
    # Corte sagital: vejiga por delante (izquierda), recto por detrás (derecha).
    ax.add_patch(Ellipse((-2.4, 1.3), 2.9, 3.0, facecolor="#f6efd9", edgecolor="#a8946a", linewidth=1))
    ax.add_patch(Polygon([(2.3, 5.5), (3.4, 5.5), (3.6, -3.6), (2.4, -3.6)], closed=True,
                         facecolor="#efe1d6", edgecolor="#a8857f", linewidth=1))
    ax.add_patch(Ellipse((0.1, 4.6), 2.6, 3.2, angle=-20, facecolor=TEJIDO, edgecolor=TEJIDO_BORDE,
                         linewidth=1))
    ax.add_patch(Polygon([(-0.75, 3.1), (0.85, 3.4), (0.85, 1.0), (-0.75, 1.0)], closed=True,
                         facecolor=CUELLO, edgecolor=TEJIDO_BORDE, linewidth=1))
    ax.add_patch(Polygon([(-0.6, 1.0), (0.75, 1.0), (0.55, -3.6), (-0.65, -3.6)], closed=True,
                         facecolor=TEJIDO, edgecolor=TEJIDO_BORDE, linewidth=1))
    tumor(ax, [(-0.6, 2.8), (0.65, 3.0), (0.65, 1.2), (-0.6, 1.1), (-1.3, 1.0), (-1.75, 1.35),
               (-1.45, 2.2)])
    ax.text(-2.6, -0.65, "Vejiga", ha="center", va="top", fontsize=15, color=INK)
    ax.text(3.0, 6.0, "Recto", ha="center", va="bottom", fontsize=15, color=INK)
    marco(ax, "IVA", "Mucosa de vejiga\no de recto")


def p_ivb(ax):
    ax.add_patch(FancyBboxPatch((-3.2, -3.4), 6.4, 9.6, boxstyle="round,pad=0.2,rounding_size=1.6",
                                facecolor="#f7f1ef", edgecolor=TEJIDO_BORDE, linewidth=1))
    for s in (-1, 1):
        ax.add_patch(Ellipse((s * 1.45, 3.7), 2.0, 3.6, facecolor="#e9eef5", edgecolor=VASO,
                             linewidth=1))
    ax.add_patch(Ellipse((-0.9, 0.9), 3.4, 1.7, facecolor="#e7d2c9", edgecolor=TEJIDO_BORDE,
                         linewidth=1))
    ax.add_patch(Polygon([(-0.22, 5.9), (0.22, 5.9), (0.22, -3.2), (-0.22, -3.2)], closed=True,
                         facecolor="#dcdad3", edgecolor=PARED, linewidth=0.8))
    for x, y in ((1.6, 4.4), (-1.2, 3.2), (-1.4, 1.0), (0.0, -1.2)):
        ax.add_patch(Circle((x, y), 0.3, facecolor=TUMOR, edgecolor="#7d2a38", linewidth=0.9,
                            zorder=5))
    ax.text(1.6, 5.85, "Pulmón", ha="center", va="bottom", fontsize=15, color=INK)
    ax.text(-0.9, -0.15, "Hígado", ha="center", va="top", fontsize=15, color=INK)
    ax.text(0.45, -1.9, "Hueso", ha="left", va="center", fontsize=15, color=INK)
    marco(ax, "IVB", "Metástasis\na distancia")


def esquema_figo():
    fig = plt.figure(figsize=(10.0, 8.0))
    paneles = [p_ib, p_iia, p_iib, p_iiia, p_iiib, p_iiic, p_iva, p_ivb]
    for i, f in enumerate(paneles):
        fila, col = divmod(i, 4)
        ax = fig.add_axes([0.005 + col * 0.25, 0.5 - fila * 0.5, 0.24, 0.49])
        f(ax)
    fig.savefig(os.path.join(OUT, "ecoe_cacu_estadios_figo2018.png"), dpi=200, bbox_inches="tight",
                pad_inches=0.08)
    plt.close(fig)


os.makedirs(OUT, exist_ok=True)
esquema_triple_toma()
esquema_figo()
