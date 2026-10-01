# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:56:06 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 2 - VISUALIZATION 4
# ADD A HIDDEN LAYER
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

MUTED = "#A8B2C7"


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, ax = plt.subplots(
    figsize=(13, 7)
)


fig.patch.set_facecolor(
    BACKGROUND
)


ax.set_facecolor(
    BACKGROUND
)


ax.set_xlim(
    0,
    13
)


ax.set_ylim(
    0,
    7
)


ax.axis(
    "off"
)


# ============================================================
# POSITIONS
# ============================================================

x1_pos = (
    2,
    5
)


x2_pos = (
    2,
    2
)


h1_pos = (
    6.2,
    4.7
)


h2_pos = (
    6.2,
    2.3
)


output_pos = (
    10.7,
    3.5
)


# ============================================================
# NODE FUNCTION
# ============================================================

def create_node(
    pos,
    radius,
    label
):

    circle = Circle(
        pos,
        radius,
        edgecolor=MUTED,
        facecolor="#203052",
        linewidth=3,
        alpha=0
    )


    ax.add_patch(
        circle
    )


    text = ax.text(
        pos[0],
        pos[1],
        label,
        ha="center",
        va="center",
        fontsize=18,
        color=WHITE,
        fontweight="bold",
        alpha=0
    )


    return circle, text


x1_node, x1_text = create_node(
    x1_pos,
    0.60,
    r"$x_1$"
)


x2_node, x2_text = create_node(
    x2_pos,
    0.60,
    r"$x_2$"
)


h1_node, h1_text = create_node(
    h1_pos,
    0.70,
    r"$h_1$"
)


h2_node, h2_text = create_node(
    h2_pos,
    0.70,
    r"$h_2$"
)


out_node, out_text = create_node(
    output_pos,
    0.80,
    "OUT"
)


# ============================================================
# CONNECTIONS
# ============================================================

connections = []


for input_pos in [
    x1_pos,
    x2_pos
]:

    for hidden_pos in [
        h1_pos,
        h2_pos
    ]:

        line, = ax.plot(
            [
                input_pos[0] + 0.60,
                hidden_pos[0] - 0.70
            ],

            [
                input_pos[1],
                hidden_pos[1]
            ],

            color=WHITE,
            linewidth=2,
            alpha=0
        )


        connections.append(
            line
        )


for hidden_pos in [
    h1_pos,
    h2_pos
]:

    line, = ax.plot(
        [
            hidden_pos[0] + 0.70,
            output_pos[0] - 0.80
        ],

        [
            hidden_pos[1],
            output_pos[1]
        ],

        color=WHITE,
        linewidth=2.5,
        alpha=0
    )


    connections.append(
        line
    )


# ============================================================
# LABELS
# ============================================================

input_label = ax.text(
    2,
    6.05,
    "INPUTS",
    ha="center",
    fontsize=15,
    color=MUTED,
    fontweight="bold",
    alpha=0
)


hidden_label = ax.text(
    6.2,
    6.05,
    "HIDDEN LAYER",
    ha="center",
    fontsize=16,
    color=YELLOW,
    fontweight="bold",
    alpha=0
)


output_label = ax.text(
    10.7,
    6.05,
    "OUTPUT",
    ha="center",
    fontsize=15,
    color=MUTED,
    fontweight="bold",
    alpha=0
)


message = ax.text(
    6.5,
    0.60,
    "",
    ha="center",
    fontsize=17,
    color=YELLOW,
    fontweight="bold"
)


fig.suptitle(
    "WHAT IF WE ADD MORE NEURONS?",
    fontsize=26,
    color=WHITE,
    fontweight="bold",
    y=0.94
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
# FADE HELPER
# ============================================================

def fade_in(
    artists,
    frames=35
):

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


        for artist in artists:

            artist.set_alpha(
                t
            )


        fig.canvas.draw_idle()

        fig.canvas.flush_events()

        plt.pause(
            PAUSE_TIME
        )


# ============================================================
# INPUTS
# ============================================================

message.set_text(
    "Start with the same two inputs."
)


fade_in(
    [
        x1_node,
        x1_text,
        x2_node,
        x2_text,
        input_label
    ]
)


plt.pause(
    0.7
)


# ============================================================
# HIDDEN LAYER
# ============================================================

message.set_text(
    "Now add two hidden neurons."
)


h1_node.set_edgecolor(
    YELLOW
)


h2_node.set_edgecolor(
    YELLOW
)


fade_in(
    [
        h1_node,
        h1_text,
        h2_node,
        h2_text,
        hidden_label
    ]
)


plt.pause(
    0.7
)


# ============================================================
# CONNECTIONS
# ============================================================

message.set_text(
    "Both hidden neurons receive both inputs."
)


fade_in(
    connections[:4]
)


plt.pause(
    0.7
)


# ============================================================
# OUTPUT
# ============================================================

message.set_text(
    "Their responses are combined by an output neuron."
)


out_node.set_edgecolor(
    BLUE
)


fade_in(
    [
        out_node,
        out_text,
        output_label
    ]
)


fade_in(
    connections[4:]
)


# ============================================================
# FINAL
# ============================================================

message.set_text(
    "Different hidden neurons can learn different features."
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