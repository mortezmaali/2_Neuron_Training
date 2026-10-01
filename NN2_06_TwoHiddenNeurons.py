# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 2 - VISUALIZATION 6
# TWO HIDDEN NEURONS
#
# External Qt window + explicit animation loop
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
GREEN = "#54E3A4"

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
# DATA POINTS
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
# TWO BOUNDARIES
# ============================================================

line_1, = ax.plot(
    [],
    [],

    color=YELLOW,

    linewidth=4,

    label="Hidden neuron 1",

    zorder=4
)


line_2, = ax.plot(
    [],
    [],

    color=GREEN,

    linewidth=4,

    label="Hidden neuron 2",

    zorder=4
)


x_values = np.linspace(
    -2.5,
    2.5,
    300
)


# Hidden neuron 1:
# x1 + x2 + 0.5 = 0
lower_line = (
    -x_values
    -
    0.5
)


# Hidden neuron 2:
# x1 + x2 - 0.5 = 0
upper_line = (
    -x_values
    +
    0.5
)


# First boundary already visible
line_1.set_data(
    x_values,
    lower_line
)


# ============================================================
# CREATE MIDDLE REGION MASK
#
# Region between:
#
#   x1 + x2 = -0.5
#
# and
#
#   x1 + x2 = +0.5
# ============================================================

grid_size = 400


grid_x = np.linspace(
    -2,
    2,
    grid_size
)


grid_y = np.linspace(
    -2,
    2,
    grid_size
)


XX, YY = np.meshgrid(
    grid_x,
    grid_y
)


SUM = (
    XX
    +
    YY
)


middle_region = (
    (
        SUM > -0.5
    )
    &
    (
        SUM < 0.5
    )
)


# Convert Boolean mask to float
region_image_data = middle_region.astype(
    float
)


# Display as an image.
#
# Start fully transparent.
region_image = ax.imshow(
    region_image_data,

    extent=[
        -2,
        2,
        -2,
        2
    ],

    origin="lower",

    cmap="Blues",

    vmin=0,
    vmax=1,

    alpha=0.0,

    interpolation="nearest",

    aspect="auto",

    zorder=1
)


# ============================================================
# TITLE AND TEXT
# ============================================================

ax.set_title(
    "TWO HIDDEN NEURONS → TWO FEATURES",

    fontsize=24,

    color=WHITE,

    fontweight="bold",

    pad=20
)


subtitle = ax.text(
    0.5,
    1.015,

    "Neuron 1 already learned one useful boundary.",

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

    fontsize=16,

    color=YELLOW,

    fontweight="bold"
)


# ============================================================
# SHOW EXTERNAL QT WINDOW
# ============================================================

plt.show(
    block=False
)


plt.pause(
    1.0
)


# ============================================================
# STAGE 1
# HOLD THE FIRST BOUNDARY
# ============================================================

message.set_text(
    "Hidden neuron 1 gives us one straight boundary."
)


fig.canvas.draw_idle()

fig.canvas.flush_events()


plt.pause(
    1.5
)


# ============================================================
# STAGE 2
# ANIMATE SECOND BOUNDARY INTO POSITION
# ============================================================

frames = 110


# Start second boundary away from final location
start_line = (
    -x_values
    +
    2.0
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


    temp_line = (
        start_line
        *
        (
            1 - t
        )
        +
        upper_line
        *
        t
    )


    line_2.set_data(
        x_values,
        temp_line
    )


    subtitle.set_text(
        "Hidden neuron 2 learns a different boundary."
    )


    message.set_text(
        "Now we have two simple linear features."
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# STAGE 3
# FADE THE REGION BETWEEN THE BOUNDARIES IN
# ============================================================

for alpha_value in np.linspace(
    0.0,
    0.20,
    55
):

    region_image.set_alpha(
        alpha_value
    )


    subtitle.set_text(
        "Together, the boundaries define a new region."
    )


    message.set_text(
        "This region could not be represented by one straight line."
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# LEGEND
# ============================================================

legend = ax.legend(
    loc="lower right",

    fontsize=11,

    facecolor=BACKGROUND,

    edgecolor=GRID
)


for text in legend.get_texts():

    text.set_color(
        WHITE
    )


# ============================================================
# FINAL MESSAGE
# ============================================================

subtitle.set_text(
    "Two neurons → two boundaries → a richer representation"
)


message.set_text(
    "Each neuron is still simple. Together, they can describe more."
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