from colors import bcolors


def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


if __name__ == '__main__':
    print(
        "the git link:https:https://github.com/haikarmi/interpolation.git\n group:Almog Babila-209477678, Hai karmi-207265687, Yagel Batito-318271863, Meril Hasid-324569714\n date :18/03/24 \n student: hai karmi id: 207265687")
    print("..........................................................................................")
    table_points = [(1.2, -3.5), (1.3, -3.69), (1.4, 0.9043), (1.5, 1.1293), (1.6, 2.3756)]

    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [-3.5, -3.69, 0.9043, 1.1293,2.3756 ]
    x_interpolate = 1.35  # The x-value where you want to interpolate
    x2_interpolate = 1.55  # The x-value where you want to interpolate
    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)
    y2_interpolate = lagrange_interpolation(x_data, y_data, x2_interpolate)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x_interpolate, "is y =", y_interpolate, bcolors.ENDC)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x2_interpolate, "is y =", y_interpolate, bcolors.ENDC)
    print(
        "https://github.com/Babilabong/tester_3_nomarit\ngroup:Almog Babila 209477678, Hai karmi 207265678, Yagel Batito 318271863, Meril Hasid 324569714\nstudent:Almog Babila 209477678")
