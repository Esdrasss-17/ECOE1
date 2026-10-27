"""Esquemas de patrones de la FCF construidos a partir de las definiciones del NICHD.

Uso: python3 herramientas/esquemas_rctg.py "<carpeta assets>"
No reproducen registros reales: cada curva se genera con los umbrales de la tabla 2
del documento (amplitud, duración y relación temporal con la contracción).
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = sys.argv[1]
FCF = "#2a78d6"
UA = "#eb6834"
INK = "#0b0b0b"
INK2 = "#52514e"
GRID = "#e4e3df"
SURF = "#fcfcfb"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": "#b9b8b2",
    "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.titlesize": 9.5, "axes.titleweight": "bold", "axes.titlecolor": INK,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
})
rng = np.random.default_rng(7)
DT = 0.25  # segundos


def variabilidad(t, amplitud):
    """Fluctuación irregular con amplitud pico a valle aproximada en lpm."""
    if amplitud == 0:
        return np.zeros_like(t)
    n = len(t)
    ruido = rng.normal(size=n)
    k = int(6 / DT)
    suave = np.convolve(ruido, np.hanning(k) / np.hanning(k).sum(), mode="same")
    suave -= suave.mean()
    escala = np.percentile(suave, 97) - np.percentile(suave, 3)
    return suave / escala * amplitud


def contraccion(t, inicio, duracion=70, pico=55, tono=12):
    x = np.clip((t - inicio) / duracion, 0, 1)
    return tono + pico * np.sin(np.pi * x) ** 2


def campana(t, inicio, duracion, profundidad):
    x = np.clip((t - inicio) / duracion, 0, 1)
    return -profundidad * np.sin(np.pi * x) ** 2


def ejes(ax, ylim, ylabel, xticks=True):
    ax.set_ylim(*ylim)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.set_ylabel(ylabel)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if not xticks:
        ax.tick_params(labelbottom=False)


def panel_con_contraccion(fig, gs, titulo, t, fcf, ua, pico_ua=None, nadir=None, nota=None):
    a1 = fig.add_subplot(gs[0])
    a2 = fig.add_subplot(gs[1], sharex=a1)
    m = t / 60
    a1.plot(m, fcf, color=FCF, linewidth=1.4)
    a2.plot(m, ua, color=UA, linewidth=1.4)
    ejes(a1, (60, 180), "FCF (lpm)", xticks=False)
    ejes(a2, (0, 80), "Contracción\n(mmHg)")
    a2.set_xlabel("Tiempo (minutos)")
    a1.set_title(titulo, loc="left")
    if pico_ua is not None:
        for a in (a1, a2):
            a.axvline(pico_ua / 60, color=INK2, linestyle=(0, (2, 2)), linewidth=0.8)
        a2.annotate("pico de la\ncontracción", (pico_ua / 60, 67), xytext=(4, 0),
                    textcoords="offset points", fontsize=7.5, color=INK2, va="center")
    if nadir is not None:
        x, y = nadir
        a1.annotate("nadir", (x / 60, y), xytext=(0, -16), textcoords="offset points",
                    ha="center", fontsize=7.5, color=INK2,
                    arrowprops=dict(arrowstyle="-|>", color=INK2, linewidth=0.8))
    if nota:
        a1.text(0.99, 0.95, nota, transform=a1.transAxes, ha="right", va="top",
                fontsize=7.5, color=INK2)
    return a1, a2


def figura_variabilidad():
    t = np.arange(0, 180, DT)
    casos = [("Ausente: amplitud indetectable", 0.4),
             ("Mínima: de 1 a 5 lpm", 4),
             ("Moderada: de 6 a 25 lpm", 15),
             ("Marcada: más de 25 lpm", 38)]
    fig, axs = plt.subplots(2, 2, figsize=(6.6, 3.9), sharex=True, sharey=True)
    for ax, (tit, amp) in zip(axs.flat, casos):
        ax.plot(t / 60, 140 + variabilidad(t, amp), color=FCF, linewidth=1.2)
        ejes(ax, (100, 180), "")
        ax.set_title(tit, loc="left")
    for ax in axs[:, 0]:
        ax.set_ylabel("FCF (lpm)")
    for ax in axs[1, :]:
        ax.set_xlabel("Tiempo (minutos)")
    fig.tight_layout()
    fig.savefig(f"{OUT}/rctg_esquema_variabilidad.png", dpi=220)
    plt.close(fig)


def figura_temprana_tardia():
    t = np.arange(0, 180, DT)
    base = 140 + variabilidad(t, 10)
    ua = contraccion(t, 50, 80)
    fig = plt.figure(figsize=(6.6, 3.3))
    g = fig.add_gridspec(2, 2, height_ratios=[2.2, 1], hspace=0.12, wspace=0.32)
    temprana = base + campana(t, 50, 80, 22)
    panel_con_contraccion(fig, [g[0, 0], g[1, 0]], "Deceleración temprana", t, temprana, ua,
                          pico_ua=90, nadir=(90, 140 - 22 - 4))
    base2 = 140 + variabilidad(t, 10)
    tardia = base2 + campana(t, 80, 90, 22)
    panel_con_contraccion(fig, [g[0, 1], g[1, 1]], "Deceleración tardía", t, tardia, ua,
                          pico_ua=90, nadir=(125, 140 - 22 - 4))
    fig.subplots_adjust(left=0.1, right=0.98, top=0.9, bottom=0.15)
    fig.savefig(f"{OUT}/rctg_esquema_temprana_tardia.png", dpi=220)
    plt.close(fig)


def figura_variable_prolongada():
    fig = plt.figure(figsize=(6.6, 3.3))
    g = fig.add_gridspec(2, 2, height_ratios=[2.2, 1], hspace=0.12, wspace=0.32)
    t = np.arange(0, 180, DT)
    fcf = 140 + variabilidad(t, 10)
    # hombro previo, caída brusca (menos de 30 s hasta el nadir), recuperación rápida y hombro posterior
    fcf += 10 * np.exp(-((t - 58) / 5) ** 2) + 10 * np.exp(-((t - 122) / 5) ** 2)
    caida = np.interp(t, [64, 76, 104, 116], [0, -55, -55, 0], left=0, right=0)
    fcf += caida
    ua = contraccion(t, 55, 75)
    panel_con_contraccion(fig, [g[0, 0], g[1, 0]], "Deceleración variable", t, fcf, ua,
                          nadir=(90, 140 - 55 - 6), nota="caída brusca, con hombros")
    t2 = np.arange(0, 360, DT)
    fcf2 = 140 + variabilidad(t2, 10)
    fcf2 += np.interp(t2, [60, 90, 240, 270], [0, -50, -50, 0], left=0, right=0)
    ua2 = contraccion(t2, 40, 80)
    a1, _ = panel_con_contraccion(fig, [g[0, 1], g[1, 1]], "Deceleración prolongada", t2, fcf2, ua2)
    a1.annotate("", xy=(60 / 60, 160), xytext=(270 / 60, 160),
                arrowprops=dict(arrowstyle="<->", color=INK2, linewidth=0.8))
    a1.text(165 / 60, 163, "de 2 a menos de 10 minutos", ha="center", fontsize=7.5, color=INK2)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.9, bottom=0.15)
    fig.savefig(f"{OUT}/rctg_esquema_variable_prolongada.png", dpi=220)
    plt.close(fig)


def figura_sinusoidal():
    t = np.arange(0, 300, DT)
    fcf = 140 + 5 * np.sin(2 * np.pi * 4 * t / 60)
    fig, ax = plt.subplots(figsize=(6.6, 1.9))
    ax.plot(t / 60, fcf, color=FCF, linewidth=1.2)
    ejes(ax, (110, 170), "FCF (lpm)")
    ax.set_xlabel("Tiempo (minutos)")
    ax.set_title("Patrón sinusoidal: 4 ciclos por minuto, amplitud de 10 lpm", loc="left")
    fig.tight_layout()
    fig.savefig(f"{OUT}/rctg_esquema_sinusoidal.png", dpi=220)
    plt.close(fig)


figura_variabilidad()
figura_temprana_tardia()
figura_variable_prolongada()
figura_sinusoidal()
