"""
PHY152 Winter 2021 Practical 8: Implementing Physics Principles in Python

This file is Copyright 2021 (c) by Arkaprava Choudhury and Luca Odisho.
Created: March 15, 2021; Edited: March 17, 2021

Side note: Arka turned 17 on March 17 2021!! Hurray!

No other persons are authorized to change/edit/modify/rewrite any portion of this file without
giving due credit and/or without prior permission. Please read all instructions clearly before
running code.

Note: For grading purposes, we expressly allow the TA to change any part of this file, as necessary,
to verify that the code is indeed functional, and follows all guidelines.

IMPORTANT NOTE: CURRENTLY, THE FILE IS SET TO RUN ACTIVITY 2 WHEN RUN IN PYTHON CONSOLE.
TO CHECK ACTIVITY 1, UNCOMMENT THE LAST FEW LINES OF CODE, AS PER THE INSTRUCTIONS GIVEN BELOW.
AFTER DOING SO, FILE WILL PRODUCE FOUR DIFFERENT PLOTS, SHOWING THE HISTORY GRAPHS AT X=0 FOR
TIMES t=32s, t=5s, t=16s, t=25s,

Note to grader: This file has been made keeping in mind Python's PEP8 Formatting Guidelines;
                As such, some aspects of the code have been modified from how they were shown in
                the Student Guide to aid readability, and also to improve the structure of code.
                The creators of this file however can confirm that the code works just as it was
                intended to, in the Student Guide. We also change the naming system from using
                camel-casing to underscores, to reflect the change in Python nomenclature
                starting from Python version 3.0 and beyond.

Note to grader: This file also uses type annotations, which is another key form of documenting
                (aka commenting) Python code, as it shows humans what to expect when running
                functions. The type annotations do not affect how the code runs in any way.

This file is created to be run on any Python versions 3.5 and above.
Note: doctest may or may not run on Python versions 3.4 and below.
"""

# This import is for adding the docstrings to all the function definitions.
# Adding type annotations helps show what the function's input and output are.
from typing import List, Tuple

# Programming Task 1A
# Since from numpy import * does not work in all versions of Python, we use the safer version below
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
#     """Function for Example 1. Takes in an input parameter x and returns x + 2.
#     >>> add_two(1)
#     3
#     """
#     return x + 2


# Programming Task 1.B.
def sine_wave_zero(amplitude: float, omega: float, time: float):
    """
    Function for Programming Task 1B
    Takes in the amplitude A, angular frequency w, and the time t, and returns the value:
    y = A sin(-wt)

    """
    return amplitude * np.sin(-omega * time)


# Example 1.2.
# We make a separate function for this, as this is also used in later examples.
# DON'T COMMENT OUT THIS FUNCTION WITHOUT COMMENTING OUT THE FUNCTION example3.
# We use example2 when implementing example3 !!
# def example2(start: float, stop: float, time_step: float, is_sine: bool) -> Tuple:
#     """
#     Helper function for Example 2 and later functions.
#     If is_sine == True, then this calculates the sine of values between start and stop, with
#     increment as time_step. If is_sine == False, it calculates the cosine instead.
#
#     To get the results for Example 1.2., call example2(0, 2, 0.5, False) in Python Console.
#     """
#     time = np.arange(start, stop, time_step)
#     if is_sine:
#         y = np.sin(time)
#     else:
#         y = np.cos(time)
#     return time, y


# Programming Task 1.D.
def task_1d(end_time: float) -> List:
    """Function for Programming Task D. Returns three lists: first list is the independent
    variable list for time, the other two are the dependent variable for the two waves.

    Make a 0.01 step difference for t, and make the list from 0 up to and not including 5.

    Values taken: amplitude = 1, omega_1 = 3 pi/2, omega_2 = 3 pi/2 + 0.3
    """
    time_step = 0.01
    time = np.arange(0, end_time, time_step)

    omega_1 = 1.5 * np.pi
    omega_2 = omega_1 + 0.3

    amplitude = 1

    dep_var_1 = sine_wave_zero(amplitude, omega_1, time)
    dep_var_2 = sine_wave_zero(amplitude, omega_2, time)

    return [time, dep_var_1, dep_var_2]


# Example 1.3.
# This is where we call the function example2
# def example3(start=0, stop=7) -> None:
#     """Function for Example 3
#     """
#     time, y_vals = example2(start, stop, time_step=0.5, is_sine=False)
#
#     # Create plot figure variable
#     fig = plt.figure()
#
#     # Create subplot
#     subplot = fig.add_subplot(111)
#
#     # Add function to subplot
#     subplot.plot(time, y_vals)
#
#     # Show plot
#     plt.show()


# Programming Task 1.E.
def task_1e(end_time: float) -> None:
    """Function for Programming Task 1E. Plots three waves, as explained in Student Guide.
    """

    # Get the lists output in Programming Task 1D
    time, y_vals_1, y_vals_2 = task_1d(end_time)

    # Create third list, by adding the previous two lists
    y_vals_3 = y_vals_1 + y_vals_2

    # Create plot figure
    fig = plt.figure()

    # Create subplot
    subplot = fig.add_subplot(111)

    # Add three functions to subplot
    subplot.plot(time, y_vals_1)
    subplot.plot(time, y_vals_2)
    subplot.plot(time, y_vals_3)

    # Show plot
    plt.show()


#########################################################################################
# Activity 2: Standing Waves Animation
#########################################################################################


# Programming Task 2.A.
def sine_wave_zero_phi(amplitude: float, omega: float, position, time: float,
                       wavenum: float) -> float:
    """Function for Programming Task 2A: takes in the correct input parameters to
    return the result of the expression y(x, t) = A sin(kx - omega t)
    """
    return amplitude * np.sin(wavenum * position - omega * time)


# Programming Task 2.B.
# This is one of the only parts of the code that uses global variables.
# As per Python PEP8 Formatting guidelines, we must minimize use of global statements as much
# as possible, in any circumstance.

# Set up the figure
fig = plt.figure()

# Set up the axes
subplot = plt.axes(xlim=(0, 10), xlabel="x", ylim=(-2, 2), ylabel="y")

# Set up the subplots we want to animate
line1, = subplot.plot([], [], lw=2)
line2, = subplot.plot([], [], lw=2)
line3, = subplot.plot([], [], lw=2)
lines = [line1, line2, line3]


# Example 2.1.
# def example_2_1(numbers: List) -> None:
#     """Example 2
#     >>> numbers = [1, 5, 3, 6]
#     >>> example_2_1(numbers)
#     1
#     5
#     3
#     6
#     """
#     for number in numbers:
#         print(number)


# Example 2.2.

# words = "hirmyrnamerisrannie"
# print(words)
# wordsbroken = words.split('r')

# DON'T UNCOMMENT THESE TWO LINES. IT IS MEANT TO BE A COMMENT.
# The following line does the same thing as in the Student Guide, but it uses a for loop instead.

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
# Make independent variable list x
x = np.linspace(0, 10, 1000)


def animate(i: int) -> List:
    """Function for Programming Task 2D. Update the functions of the three plots.
    """

    # y1 = list to evaluate your sine wave with A= 1, angular frequency 2π, and wave number π/2.
    y1 = sine_wave_zero_phi(1, 2 * np.pi, x, 0.01 * i, 0.5 * np.pi)

    # y2 = list to evaluate your sine wave with A= 1, angular frequency -2π, and wave number π/2.
    y2 = sine_wave_zero_phi(1, -2 * np.pi, x, 0.01 * i, 0.5 * np.pi)

    # y3 = sum of y1 and y2
    y3 = y1 + y2

    # Create a 2-dimensional list variable
    wave_functions = [[x, y1], [x, y2], [x, y3]]

    # use line.set_data to set the appropriate function from the wave_functions variable
    for index in range(len(wave_functions)):
        lines[index].set_data(wave_functions[index][0], wave_functions[index][1])

    return lines


# animate!
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# show plot
plt.show()

# Uncomment lines 288 through 293 to check Activity 1.
# if __name__ == '__main__':
#     task_1e(end_time=32)
#     task_1e(end_time=5)
#     task_1e(end_time=16)
#     task_1e(end_time=25)
#     # If you want to test the example functions and the functions with docstrings, uncomment them
#     # and uncomment lines 296 and 297.
#     # import doctest
#     # doctest.testmod()
