import numpy as np
import math
from sympy import symbols, diff, sin, cos, tan



def romberg_integration(f, a, b, n):
    """
    Approximate the integral of f(x) from a to b using Romberg Integration.

    :param f: The function to integrate.
    :param a: Lower limit of integration.
    :param b: Upper limit of integration.
    :param n: Number of iterations.
    :return: Approximation of the integral.
    """
    # Initialize R array
    R = np.zeros((n, n))

    # Trapezoidal rule with only first iteration
    h = b - a
    R[0, 0] = 0.5 * h * (f(a) + f(b))

    for i in range(1, n):
        # Richardson extrapolation
        h /= 2
        total = 0
        for k in range(1, 2 ** i, 2):
            total += f(a + k * h)
        R[i, 0] = 0.5 * R[i - 1, 0] + total * h

        # Romberg recursion
        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4 ** j) - 1)

    print(R)

    return R[n - 1, n - 1]


# Example function to integrate
def example_function(x):
    return ((2 * (x ** 2)) + (cos(2 * (math.e ** (-2 * x))))) / ((2 * (x ** 3)) + (x ** 2) - 6)


# Example usage

a = -1 # Lower limit
b = 0.7  # Upper limit
n = 13  # Number of iterations
approximation = romberg_integration(example_function, a, b, n)
print("Approximation of integral:", approximation)
print(
    "the git link:https:https://github.com/haikarmi/interpolation.git\n group:Almog Babila-209477678, Hai karmi-207265687, Yagel Batito-318271863, Meril Hasid-324569714\n date :18/03/24 \n student: hai karmi id: 207265687")
print("..........................................................................................")
