# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 2 - VISUALIZATION 1
# THE XOR PROBLEM
#
# Designed for Anaconda + Spyder.
# Forces Matplotlib to use a separate Qt window.
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
# CREATE XOR DATA
# ============================================================

rng = np.random.default_rng(
    RANDOM_SEED
)


bottom_left = rng.normal(
    loc=(-1.0, -1.0),
    scale=(0.22, 0.22),
    size=(N_PER_CLUSTER, 2)
)


top_left = rng.normal(
    loc=(-1.0, 1.0),
    scale=(0.22, 0.22),
    size=(N_PER_CLUSTER, 2)
)


bottom_right = rng.normal(
    loc=(1.0, -1.0),
    scale=(0.22, 0.22),
    size=(N_PER_CLUSTER, 2)
)


top_right = rng.normal(
    loc=(1.0, 1.0),
    scale=(0.22, 0.22),
    size=(N_PER_CLUSTER, 2)
)


# Conventional XOR-style diagonal classes:
#
# RED  = bottom-left + top-right
# BLUE = top-left + bottom-right

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
    r"$x_1$  /  Input 1",
    fontsize=16,
    color=WHITE
)


ax.set_ylabel(
    r"$x_2$  /  Input 2",
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
# EMPTY SCATTER OBJECTS
# ============================================================

scatter_bl = ax.scatter(
    [],
    [],
    s=130,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.8,
    zorder=5
)


scatter_tl = ax.scatter(
    [],
    [],
    s=130,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.8,
    zorder=5
)


scatter_br = ax.scatter(
    [],
    [],
    s=130,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.8,
    zorder=5
)


scatter_tr = ax.scatter(
    [],
    [],
    s=130,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.8,
    zorder=5
)


# ============================================================
# TEXT
# ============================================================

ax.set_title(
    "A NEW PROBLEM: XOR",
    fontsize=25,
    color=WHITE,
    fontweight="bold",
    pad=20
)


subtitle = ax.text(
    0.5,
    1.015,
    "",
    transform=ax.transAxes,
    ha="center",
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
# SHOW EXTERNAL WINDOW
# ============================================================

plt.show(
    block=False
)


plt.pause(
    0.6
)


# ============================================================
# HELPER
# ============================================================

def reveal_cluster(
    scatter_object,
    points,
    label_text
):

    for i in range(
        1,
        len(points) + 1
    ):

        scatter_object.set_offsets(
            points[:i]
        )

        subtitle.set_text(
            label_text
        )

        fig.canvas.draw_idle()

        fig.canvas.flush_events()

        plt.pause(
            PAUSE_TIME
        )


# ============================================================
# REVEAL THE FOUR CORNERS
# ============================================================

reveal_cluster(
    scatter_bl,
    bottom_left,
    "Bottom-left → RED"
)


plt.pause(
    0.4
)


reveal_cluster(
    scatter_tl,
    top_left,
    "Top-left → BLUE"
)


plt.pause(
    0.4
)


reveal_cluster(
    scatter_br,
    bottom_right,
    "Bottom-right → BLUE"
)


plt.pause(
    0.4
)


reveal_cluster(
    scatter_tr,
    top_right,
    "Top-right → RED"
)


# ============================================================
# FINAL MESSAGE
# ============================================================

subtitle.set_text(
    "Opposite corners belong to the same class"
)


message.set_text(
    "Can one neuron still separate RED from BLUE?"
)


fig.canvas.draw_idle()

fig.canvas.flush_events()


# ============================================================
# KEEP WINDOW OPEN
# ============================================================

while plt.fignum_exists(
    fig.number
):

    fig.canvas.flush_events()

    plt.pause(
        0.05
    )