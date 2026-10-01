# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:57:18 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 2 - VISUALIZATION 5
# HIDDEN NEURON 1
# ============================================================


# ============================================================
# FORCE EXTERNAL QT WINDOW
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")


import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# SETTINGS
# ============================================================

RANDOM_SEED = 5
N_PER_CLUSTER = 18

PAUSE_TIME = 0.04


BACKGROUND = "#090D18"

RED = "#FF5369"
BLUE = "#4D9FFF"

WHITE = "#F5F7FF"
YELLOW = "#FFD166"

MUTED = "#A8B2C7"
GRID = "#33405A"


# ============================================================
# XOR DATA
# ============================================================

rng = np.random.default_rng(
    RANDOM_SEED
)


bottom_left = rng.normal(
    (-1, -1),
    0.22,
    size=(N_PER_CLUSTER, 2)
)


top_left = rng.normal(
    (-1, 1),
    0.22,
    size=(N_PER_CLUSTER, 2)
)


bottom_right = rng.normal(
    (1, -1),
    0.22,
    size=(N_PER_CLUSTER, 2)
)


top_right = rng.normal(
    (1, 1),
    0.22,
    size=(N_PER_CLUSTER, 2)
)


red_points = np.vstack(
    [
        bottom_left,
        top_right
    ]
)


blue_points = np.vstack(
    [
        top_left,
        bottom_right
    ]
)


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, ax = plt.subplots(
    figsize=(12, 8)
)


fig.patch.set_facecolor(
    BACKGROUND
)


ax.set_facecolor(
    BACKGROUND
)


ax.set_xlim(
    -2,
    2
)


ax.set_ylim(
    -2,
    2
)


ax.set_xlabel(
    r"$x_1$",
    fontsize=16,
    color=WHITE
)


ax.set_ylabel(
    r"$x_2$",
    fontsize=16,
    color=WHITE
)


ax.tick_params(
    colors=MUTED
)


ax.grid(
    alpha=0.20,
    color=GRID,
    linestyle=":"
)


for spine in ax.spines.values():

    spine.set_color(
        GRID
    )


# ============================================================
# POINTS
# ============================================================

ax.scatter(
    red_points[:, 0],
    red_points[:, 1],
    s=120,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.7,
    zorder=5
)


ax.scatter(
    blue_points[:, 0],
    blue_points[:, 1],
    s=120,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.7,
    zorder=5
)


# ============================================================
# BOUNDARY
# ============================================================

boundary_line, = ax.plot(
    [],
    [],
    color=YELLOW,
    linewidth=4,
    zorder=4
)


# ============================================================
# TEXT
# ============================================================

ax.set_title(
    "HIDDEN NEURON 1",
    fontsize=25,
    color=WHITE,
    fontweight="bold",
    pad=20
)


equation_text = ax.text(
    0.5,
    1.015,
    r"Boundary:  $x_1+x_2+0.5=0$",
    transform=ax.transAxes,
    ha="center",
    fontsize=16,
    color=YELLOW
)


message = ax.text(
    0.5,
    0.05,
    "",
    transform=ax.transAxes,
    ha="center",
    fontsize=15,
    color=MUTED
)


# ============================================================
# SHOW WINDOW
# ============================================================

plt.show(
    block=False
)


plt.pause(
    0.7
)


# ============================================================
# ANIMATE BOUNDARY
# ============================================================

frames = 110


x_values = np.linspace(
    -2.5,
    2.5,
    300
)


for frame in range(
    frames
):

    progress = (
        frame
        /
        (
            frames - 1
        )
    )


    # Smoothstep
    t = (
        progress
        *
        progress
        *
        (
            3
            -
            2
            *
            progress
        )
    )


    # Start almost horizontal
    start_slope = 0.0
    start_intercept = 1.5


    # Final:
    # x1 + x2 + 0.5 = 0
    # x2 = -x1 - 0.5

    final_slope = -1.0
    final_intercept = -0.5


    slope = (
        start_slope
        *
        (
            1 - t
        )
        +
        final_slope
        *
        t
    )


    intercept = (
        start_intercept
        *
        (
            1 - t
        )
        +
        final_intercept
        *
        t
    )


    y_values = (
        slope
        *
        x_values
        +
        intercept
    )


    boundary_line.set_data(
        x_values,
        y_values
    )


    message.set_text(
        "Hidden neuron 1 learns one useful linear feature."
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# FINAL
# ============================================================

message.set_text(
    "It still cannot solve XOR alone — and it does not need to."
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