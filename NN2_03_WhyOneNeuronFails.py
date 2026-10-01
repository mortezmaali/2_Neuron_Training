# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:55:20 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 2 - VISUALIZATION 3
# WHY ONE NEURON FAILS
# ============================================================


# ============================================================
# FORCE EXTERNAL QT WINDOW
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")


import matplotlib.pyplot as plt


# ============================================================
# STYLE
# ============================================================

BACKGROUND = "#090D18"

WHITE = "#F5F7FF"
YELLOW = "#FFD166"

MUTED = "#A8B2C7"


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, ax = plt.subplots(
    figsize=(12, 7)
)


fig.patch.set_facecolor(
    BACKGROUND
)


ax.set_facecolor(
    BACKGROUND
)


ax.set_xlim(
    0,
    1
)


ax.set_ylim(
    0,
    1
)


ax.axis(
    "off"
)


# ============================================================
# TITLE
# ============================================================

title = ax.text(
    0.5,
    0.91,
    "WHY DOES ONE NEURON FAIL?",
    ha="center",
    fontsize=26,
    color=WHITE,
    fontweight="bold"
)


eq1 = ax.text(
    0.5,
    0.72,
    "",
    ha="center",
    fontsize=34,
    color=WHITE
)


eq2 = ax.text(
    0.5,
    0.58,
    "",
    ha="center",
    fontsize=30,
    color=WHITE
)


arrow = ax.text(
    0.5,
    0.47,
    "",
    ha="center",
    fontsize=30,
    color=MUTED
)


boundary_eq = ax.text(
    0.5,
    0.35,
    "",
    ha="center",
    fontsize=32,
    color=YELLOW,
    fontweight="bold"
)


explanation = ax.text(
    0.5,
    0.22,
    "",
    ha="center",
    fontsize=18,
    color=MUTED
)


conclusion = ax.text(
    0.5,
    0.09,
    "",
    ha="center",
    fontsize=22,
    color=YELLOW,
    fontweight="bold"
)


# ============================================================
# SHOW WINDOW
# ============================================================

plt.show(
    block=False
)


plt.pause(
    0.8
)


# ============================================================
# REVEAL EQUATIONS
# ============================================================

eq1.set_text(
    r"$z=w_1x_1+w_2x_2+b$"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()

plt.pause(
    1.6
)


eq2.set_text(
    r"$p=\sigma(z)$"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()

plt.pause(
    1.4
)


arrow.set_text(
    r"$\downarrow$"
)


boundary_eq.set_text(
    r"$w_1x_1+w_2x_2+b=0$"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()

plt.pause(
    1.8
)


explanation.set_text(
    "With two inputs, this decision boundary is always a straight line."
)


fig.canvas.draw_idle()
fig.canvas.flush_events()

plt.pause(
    1.8
)


conclusion.set_text(
    "XOR IS NOT LINEARLY SEPARABLE"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


# ============================================================
# KEEP OPEN
# ============================================================

while plt.fignum_exists(
    fig.number
):

    fig.canvas.flush_events()

    plt.pause(
        0.05
    )