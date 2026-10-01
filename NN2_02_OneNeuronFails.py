# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:54:15 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 2 - VISUALIZATION 2
# ONE NEURON TRIES TO SOLVE XOR
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

PAUSE_TIME = 0.035

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
# DATA
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
# DECISION LINE
# ============================================================

decision_line, = ax.plot(
    [],
    [],
    color=WHITE,
    linewidth=4,
    zorder=4
)


# ============================================================
# TEXT
# ============================================================

ax.set_title(
    "CAN ONE NEURON SOLVE XOR?",
    fontsize=25,
    color=WHITE,
    fontweight="bold",
    pad=20
)


top_text = ax.text(
    0.5,
    0.96,
    "One neuron = one straight decision boundary",
    transform=ax.transAxes,
    ha="center",
    va="top",
    fontsize=15,
    color=MUTED
)


message = ax.text(
    0.5,
    0.05,
    "",
    transform=ax.transAxes,
    ha="center",
    fontsize=17,
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
    0.7
)


# ============================================================
# ANIMATE
# ============================================================

frames = 260


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


    angle = (
        progress
        *
        np.pi
    )


    # Translation of line along its normal
    offset = (
        0.55
        *
        np.sin(
            progress
            *
            4
            *
            np.pi
        )
    )


    # Normal to line
    nx = np.cos(
        angle
    )

    ny = np.sin(
        angle
    )


    # Direction along line
    dx = -ny
    dy = nx


    center_x = (
        offset
        *
        nx
    )


    center_y = (
        offset
        *
        ny
    )


    length = 4.0


    x_values = np.array(
        [
            center_x
            -
            length
            *
            dx,

            center_x
            +
            length
            *
            dx
        ]
    )


    y_values = np.array(
        [
            center_y
            -
            length
            *
            dy,

            center_y
            +
            length
            *
            dy
        ]
    )


    decision_line.set_data(
        x_values,
        y_values
    )


    if progress < 0.33:

        message.set_text(
            "Rotate the boundary..."
        )

    elif progress < 0.66:

        message.set_text(
            "Move the boundary..."
        )

    else:

        message.set_text(
            "Try another orientation..."
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
    "NO SINGLE STRAIGHT LINE CAN SOLVE XOR"
)


top_text.set_text(
    "The problem is not bad training — the model is too simple."
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