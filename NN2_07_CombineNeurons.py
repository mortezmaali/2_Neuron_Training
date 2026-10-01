# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 19:00:58 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 2 - VISUALIZATION 7
# COMBINE THE HIDDEN NEURONS
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
# SIGMOID
# ============================================================

def sigmoid(z):

    z = np.clip(
        z,
        -30,
        30
    )

    return (
        1
        /
        (
            1
            +
            np.exp(
                -z
            )
        )
    )


# ============================================================
# EXAMPLE INPUT
#
# Pick one BLUE XOR point:
# (-1, +1)
# ============================================================

x1 = -1.0
x2 = 1.0


# ============================================================
# HIDDEN RESPONSES
# ============================================================

sharpness = 8.0


z1 = (
    sharpness
    *
    (
        x1
        +
        x2
        +
        0.5
    )
)


h1 = sigmoid(
    z1
)


z2 = (
    sharpness
    *
    (
        x1
        +
        x2
        -
        0.5
    )
)


h2 = sigmoid(
    z2
)


# Output is high for the middle region:
# h1 ≈ 1 and h2 ≈ 0

output_z = (
    8.0
    *
    h1
    -
    8.0
    *
    h2
    -
    4.0
)


p = sigmoid(
    output_z
)


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
# POSITIONS
# ============================================================

x1_pos = (
    2,
    5.5
)


x2_pos = (
    2,
    2.5
)


h1_pos = (
    6,
    5.2
)


h2_pos = (
    6,
    2.8
)


output_pos = (
    10.8,
    4.0
)


# ============================================================
# CONNECTIONS
# ============================================================

input_lines = []


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

            color=MUTED,
            linewidth=2,
            alpha=0.25
        )


        input_lines.append(
            line
        )


hidden_lines = []


for hidden_pos in [
    h1_pos,
    h2_pos
]:

    line, = ax.plot(
        [
            hidden_pos[0] + 0.70,
            output_pos[0] - 0.85
        ],

        [
            hidden_pos[1],
            output_pos[1]
        ],

        color=MUTED,
        linewidth=2,
        alpha=0.25
    )


    hidden_lines.append(
        line
    )


# ============================================================
# NODE CREATION
# ============================================================

def create_node(
    pos,
    radius,
    label
):

    circle = Circle(
        pos,
        radius,
        facecolor="#203052",
        edgecolor=MUTED,
        linewidth=3
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
        fontweight="bold"
    )


    return circle, text


x1_node, _ = create_node(
    x1_pos,
    0.60,
    r"$x_1$"
)


x2_node, _ = create_node(
    x2_pos,
    0.60,
    r"$x_2$"
)


h1_node, _ = create_node(
    h1_pos,
    0.70,
    r"$h_1$"
)


h2_node, _ = create_node(
    h2_pos,
    0.70,
    r"$h_2$"
)


out_node, _ = create_node(
    output_pos,
    0.85,
    "OUT"
)


# ============================================================
# VALUES
# ============================================================

ax.text(
    2,
    6.45,
    f"x₁ = {x1:+.1f}",
    ha="center",
    fontsize=16,
    color=MUTED
)


ax.text(
    2,
    1.55,
    f"x₂ = {x2:+.1f}",
    ha="center",
    fontsize=16,
    color=MUTED
)


h1_value = ax.text(
    6,
    6.20,
    "",
    ha="center",
    fontsize=17,
    color=YELLOW,
    fontweight="bold"
)


h2_value = ax.text(
    6,
    1.80,
    "",
    ha="center",
    fontsize=17,
    color=GREEN,
    fontweight="bold"
)


output_value = ax.text(
    10.8,
    2.40,
    "",
    ha="center",
    fontsize=22,
    color=BLUE,
    fontweight="bold"
)


# ============================================================
# EQUATIONS
# ============================================================

ax.text(
    6,
    7.10,
    r"$h_1=\sigma(z_1)$        $h_2=\sigma(z_2)$",
    ha="center",
    fontsize=19,
    color=WHITE
)


ax.text(
    10.8,
    5.75,
    r"$p=\sigma(v_1h_1+v_2h_2+b_o)$",
    ha="center",
    fontsize=18,
    color=WHITE
)


message = ax.text(
    7,
    0.60,
    "",
    ha="center",
    fontsize=17,
    color=YELLOW,
    fontweight="bold"
)


fig.suptitle(
    "THE OUTPUT NEURON COMBINES THE FEATURES",
    fontsize=25,
    color=WHITE,
    fontweight="bold",
    y=0.95
)


# ============================================================
# SHOW WINDOW
# ============================================================

plt.show(
    block=False
)


plt.pause(
    1.0
)


# ============================================================
# STAGE 1 — INPUT SIGNAL
# ============================================================

frames = 40


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


    x1_node.set_edgecolor(
        BLUE
    )


    x2_node.set_edgecolor(
        BLUE
    )


    x1_node.set_linewidth(
        3
        +
        3
        *
        t
    )


    x2_node.set_linewidth(
        3
        +
        3
        *
        t
    )


    for line in input_lines:

        line.set_color(
            BLUE
        )

        line.set_alpha(
            0.25
            +
            0.75
            *
            t
        )


    message.set_text(
        "The inputs are sent to both hidden neurons."
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# STAGE 2 — HIDDEN RESPONSES
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


    h1_node.set_edgecolor(
        YELLOW
    )


    h2_node.set_edgecolor(
        GREEN
    )


    h1_node.set_linewidth(
        3
        +
        3
        *
        t
    )


    h2_node.set_linewidth(
        3
        +
        3
        *
        t
    )


    h1_value.set_text(
        f"h₁ = {h1:.3f}"
    )


    h2_value.set_text(
        f"h₂ = {h2:.3f}"
    )


    message.set_text(
        "Each hidden neuron produces a different feature response."
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# STAGE 3 — SEND RESPONSES TO OUTPUT
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


    hidden_lines[0].set_color(
        YELLOW
    )


    hidden_lines[1].set_color(
        GREEN
    )


    for line in hidden_lines:

        line.set_alpha(
            0.25
            +
            0.75
            *
            t
        )


        line.set_linewidth(
            2
            +
            2
            *
            t
        )


    out_node.set_edgecolor(
        BLUE
    )


    out_node.set_linewidth(
        3
        +
        3
        *
        t
    )


    message.set_text(
        "The output neuron combines those hidden features."
    )


    fig.canvas.draw_idle()

    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# FINAL PREDICTION
# ============================================================

output_value.set_text(
    f"p = {p:.3f}\n\nPREDICTION: BLUE"
)


message.set_text(
    "Simple neurons working together can solve a richer problem."
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