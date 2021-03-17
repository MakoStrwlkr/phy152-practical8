"""
PHY152 Winter 2021 Practical 8: Implementing Physics Principles in Python

This file is Copyright 2021 (c) by Arkaprava Choudhury and Luca Odisho.
No other persons are authorized to change/edit/modify/rewrite any portion of this file without
giving due credit and/or without prior permission.

Note: For grading purposes, we expressly allow the TA to change any part of this file, as necessary,
to verify that the code is indeed functional, and follows all guidelines.
"""
from typing import List, Tuple

# Programming Task 1A
import numpy as np

# Programming Task 1C
import matplotlib.pyplot as plt

# Programming Task 2E
from matplotlib import animation

#########################################################################################
# Activity 1: Beats History Graph
#########################################################################################

# Example 1.1.
# def add_two(x: float) -> float:
#     """Function for Example 1
#     >>> add_two(1)
#     3
#     """
#     return x + 2


# Programming Task 1.B.
def sine_wave_zero(amplitude: float, omega: float, time: float) -> float:
    """Function for Programming Task 1B"""
    return amplitude * np.sin(omega * time)


# Example 1.2.
def example2(start: float, stop: float, time_step: float, is_sine: bool) -> Tuple:
    """Helper function for Example 2 and later functions"""
    time = np.arange(start, stop, time_step)
    if is_sine:
        y = np.sin(time)
    else:
        y = np.cos(time)
    return time, y


# Programming Task 1.D.
def task_1d() -> List:
    """Function for Programming Task D

    Values taken: amplitude = 1, omega_1 = 3 pi/2, omega_2 = 3 pi/2 + 0.3
    """
    time_step = 0.01
    time = np.arange(0, 5, time_step)

    omega_1 = 1.5 * np.pi
    omega_2 = omega_1 + 0.3

    amplitude = 1

    dep_var_1 = sine_wave_zero(amplitude, omega_1, time)
    dep_var_2 = sine_wave_zero(amplitude, omega_2, time)

    return [time, dep_var_1, dep_var_2]


# Example 1.3.
def example3(start=0, stop=7) -> None:
    """Function for Example 3"""
    time, y_vals = example2(start, stop, time_step=0.5, is_sine=False)
    fig = plt.figure()
    subplot = fig.add_subplot(111)
    subplot.plot(time, y_vals)
    plt.show()


# Programming Task 1.E.
def task_1e() -> None:
    """Function for Programming Task 1E"""
    time, y_vals_1, y_vals_2 = task_1d()

    # Create third list, by adding the previous two lists
    y_vals_3 = y_vals_1 + y_vals_2

    fig = plt.figure()
    subplot = fig.add_subplot(111)

    subplot.plot(time, y_vals_1)
    subplot.plot(time, y_vals_2)
    subplot.plot(time, y_vals_3)

    plt.show()


#########################################################################################
# Activity 2
#########################################################################################


# Programming Task 2.A.
def sine_wave_zero_phi(amplitude: float, omega: float, position, time: float,
                       wavenum: float) -> float:
    """Function for Programming Task 2A: takes in the correct input parameters to
    return the result of the expression y(x, t) = A sin(kx - omega t)
    """
    return amplitude * np.sin(wavenum * position - omega * time)


# Programming Task 2.B.
fig = plt.figure()
subplot = plt.axes(xlim=(0, 10), xlabel="x", ylim=(-2, 2), ylabel="y")
line1, = subplot.plot([], [], lw=2)
line2, = subplot.plot([], [], lw=2)
line3, = subplot.plot([], [], lw=2)
lines = [line1, line2, line3]


# Example 2.1.
def example_2_1(numbers: List) -> None:
    """Example 2
    >>> numbers = [1, 5, 3, 6]
    >>> example_2_1(numbers)
    1
    5
    3
    6
    """
    for number in numbers:
        print(number)


# Example 2.2.

# words = "hirmyrnamerisrannie"
# print(words)
# wordsbroken = words.split('r')
# for i in range(len(wordsbroken)):
#     print(wordsbroken[i])


# Programming Task 2.C.

def init() -> List:
    """Function for Programming Task 2C"""
    for line in lines:
        line.set_data([], [])
    return lines


# Example 2.3
def example_2_3(lst: List) -> None:
    """Function for Example 2.3.
    >>> listy = [[2, 4], [3, 8], [6, 7]]
    >>> print("Old 1st list: ", listy[0][0], listy[0][1])
    Old 1st list:  2 4
    >>> print("Old 2nd list: ", listy[1][0], listy[1][1])
    Old 2nd list:  3 8
    >>> print("Old 3rd list: ", listy[2][0], listy[2][1])
    Old 3rd list:  6 7
    >>> example_2_3(listy)
    >>> print("New 1st list: ", listy[0][0], listy[0][1])
    New 1st list:  2 7
    >>> print("New 2nd list: ", listy[1][0], listy[1][1])
    New 2nd list:  3 7
    >>> print("New 3rd list: ", listy[2][0], listy[2][1])
    New 3rd list:  6 7
    """
    for i in range(len(lst)):
        lst[i][1] = 7


# Programming Task 2.D.
x = np.linspace(0, 10, 1000)


def animate(i: int) -> List:
    """Function for Programming Task 2D"""
    y1 = sine_wave_zero_phi(1, 2 * np.pi, x, 0.01 * i, 0.5 * np.pi)
    y2 = sine_wave_zero_phi(1, -2 * np.pi, x, 0.01 * i, 0.5 * np.pi)
    y3 = y1 + y2

    wave_functions = [[x, y1], [x, y2], [x, y3]]

    for index in range(len(wave_functions)):
        lines[index].set_data(wave_functions[index][0], wave_functions[index][1])

    return lines


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
plt.show()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
