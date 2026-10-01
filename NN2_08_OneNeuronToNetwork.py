# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 19:02:15 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 2 - VISUALIZATION 8
# FROM ONE NEURON TO A NETWORK
# ============================================================


# ============================================================
# FORCE EXTERNAL QT WINDOW
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")


import matplotlib.pyplot as plt
from matplotlib.patches import Circle


# ============================================================
# SETTINGS
# ============================================================

PAUSE_TIME = 0.04


BACKGROUND = "#090D18"

WHITE = "#F5F7FF"

BLUE = "#4D9FFF"
YELLOW = "#FFD166"
GREEN = "#54E3A4"

MUTED = "#A8B2C7"


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, ax = plt.subplots(
    figsize=(14, 8)
)


fig.patch.set_facecolor(
    BACKGROUND
)


ax.set_facecolor(
    BACKGROUND
)


ax.set_xlim(
    0,
    14
)


ax.set_ylim(
    0,
    8
)


ax.axis(
    "off"
)


# ============================================================
# TITLE
# ============================================================

ax.text(
    7,
    7.25,
    "FROM ONE NEURON TO A NETWORK",
    ha="center",
    fontsize=28,
    color=WHITE,
    fontweight="bold"
)


message = ax.text(
    7,
    0.72,
    "",
    ha="center",
    fontsize=18,
    color=YELLOW,
    fontweight="bold"
)


next_episode = ax.text(
    7,
    0.25,
    "",
    ha="center",
    fontsize=15,
    color=MUTED
)


# ============================================================
# SINGLE NEURON
# ============================================================

single_node = Circle(
    (
        7,
        4
    ),
    0.90,
    facecolor="#203052",
    edgecolor=BLUE,
    linewidth=4
)


ax.add_patch(
    single_node
)


single_text = ax.text(
    7,
    4,
    "1",
    ha="center",
    va="center",
    fontsize=27,
    color=WHITE,
    fontweight="bold"
)


single_label = ax.text(
    7,
    5.45,
    "ONE NEURON",
    ha="center",
    fontsize=20,
    color=WHITE,
    fontweight="bold"
)


boundary_text = ax.text(
    7,
    2.65,
    "One straight boundary",
    ha="center",
    fontsize=18,
    color=YELLOW
)


# ============================================================
# FUTURE NETWORK
# ============================================================

positions = [
    (3.0, 5.2),
    (3.0, 2.8),

    (7.0, 5.3),
    (7.0, 2.7),

    (11.0, 4.0)
]


network_nodes = []


for pos in positions:

    node = Circle(
        pos,
        0.55,
        facecolor="#203052",
        edgecolor=BLUE,
        linewidth=0,
        alpha=0
    )


    ax.add_patch(
        node
    )


    network_nodes.append(
        node
    )


# ============================================================
# CONNECTIONS
# ============================================================

network_lines = []


for start in positions[:2]:

    for end in positions[2:4]:

        line, = ax.plot(
            [
                start[0] + 0.50,
                end[0] - 0.50
            ],

            [
                start[1],
                end[1]
            ],

            color=WHITE,
            linewidth=2,
            alpha=0
        )


        network_lines.append(
            line
        )


for start in positions[2:4]:

    end = positions[4]


    line, = ax.plot(
        [
            start[0] + 0.50,
            end[0] - 0.50
        ],

        [
            start[1],
            end[1]
        ],

        color=WHITE,
        linewidth=2,
        alpha=0
    )


    network_lines.append(
        line
    )


# ============================================================
# NETWORK LABELS
# ============================================================

input_label = ax.text(
    3,
    6.15,
    "INPUTS",
    ha="center",
    fontsize=15,
    color=MUTED,
    fontweight="bold",
    alpha=0
)


hidden_label = ax.text(
    7,
    6.15,
    "HIDDEN LAYER",
    ha="center",
    fontsize=15,
    color=YELLOW,
    fontweight="bold",
    alpha=0
)


output_label = ax.text(
    11,
    6.15,
    "OUTPUT",
    ha="center",
    fontsize=15,
    color=MUTED,
    fontweight="bold",
    alpha=0
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
# ONE NEURON MESSAGE
# ============================================================

message.set_text(
    "ONE NEURON → ONE STRAIGHT BOUNDARY"
)


fig.canvas.draw_idle()

fig.canvas.flush_events()


plt.pause(
    2.2
)


# ============================================================
# FADE SINGLE NEURON OUT
# ============================================================

frames = 50


for frame in range(
    frames
):

    t = (
        frame
        /
        (
            frames - 1
        )
    )


    alpha = (
        1
        -
        t
    )


    single_node.set_alpha(
        alpha
    )


    single_text.set_alpha(
        alpha
    )


    single_label.set_alpha(
        alpha
    )


    boundary_text.set_alpha(
        alpha
    )


    message.set_text(
        "But some problems need more than one feature..."
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# BUILD NETWORK
# ============================================================

for frame in range(
    frames
):

    t = (
        frame
        /
        (
            frames - 1
        )
    )


    for node in network_nodes:

        node.set_alpha(
            t
        )


        node.set_linewidth(
            3
            *
            t
        )


    for line in network_lines:

        line.set_alpha(
            0.75
            *
            t
        )


    input_label.set_alpha(
        t
    )


    hidden_label.set_alpha(
        t
    )


    output_label.set_alpha(
        t
    )


    message.set_text(
        "ADD MORE NEURONS → LEARN MORE FEATURES"
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# PULSE HIDDEN LAYER
# ============================================================

for frame in range(
    70
):

    pulse = (
        3
        +
        2
        *
        abs(
            __import__("math").sin(
                frame
                *
                0.12
            )
        )
    )


    network_nodes[2].set_edgecolor(
        YELLOW
    )


    network_nodes[3].set_edgecolor(
        GREEN
    )


    network_nodes[2].set_linewidth(
        pulse
    )


    network_nodes[3].set_linewidth(
        pulse
    )


    message.set_text(
        "Each neuron stays simple. The power comes from combining them."
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# EPISODE 3 TEASER
# ============================================================

next_episode.set_text(
    "NEXT: How does a multi-layer network know which weights to change?"
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