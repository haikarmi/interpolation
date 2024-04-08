import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, sin, cos, tan

import sympy as sp

from colors import bcolors
from sympy.utilities.lambdify import lambdify

x = sp.symbols('x')


def simpson_max_error(f, Upper_bound, a, b, n):
    h = (b - a) / n
    for i in range(4):
        f = sp.diff(f)

    f = lambdify(x, f)
    return (1 / 180) * (h ** 4) * (b - a) * f(Upper_bound)


def simpsons_rule(f, a, b, n):
    """
    Simpson's Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals (must be even).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    f = lambdify(x, f)
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n

    integral = f(a) + f(b)  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= (h / 3)

    return integral


if __name__ == '__main__':
    print(
        "the git link:https:https://github.com/haikarmi/interpolation.git\n group:Almog Babila-209477678, Hai karmi-207265687, Yagel Batito-318271863, Meril Hasid-324569714\n date :08/04/24 \n student: hai karmi id: 207265687")
    print("..........................................................................................")

    f = ((2 * (x ** 2)) + (cos(2 * (math.e ** (-2 * x))))) / ((2 * (x ** 3)) + (x ** 2) - 6)
    g = lambda x: math.e ** (x ** 2)
    n = 500
    a = -1
    b = 0.7
    error = simpson_max_error(f, b, a, b, n)
    # print(error)
    if (error > 0.001):
        print("max error in Simpson's is: ", error)

    # print(f" Division into n={n} sections ")
    integral = simpsons_rule(f, a, b, n)
    # integral += simpsons_rule(f, c, d, n)
    print(bcolors.OKBLUE, f"Numerical Integration of definite integral in range [{a},{b}] is {integral}", bcolors.ENDC)
.