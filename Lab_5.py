# Lab 5: Functions

import sympy

# Easy tasks


def function_evaluator(m, b, x):
    return m * x + b


print(function_evaluator(2, 3, 4))


def domain_range_identifier(set_of_pairs):
    set_domain = []
    set_range = []
    for i in set_of_pairs:
        set_domain.append(i[0])
        set_range.append(i[1])
    return f"Domain: {set_domain}\nRange:{set_range}"


print(domain_range_identifier([(1, 2), (3, 6), (4, 8)]))


def function_identifier(list_of_points):
    even = True
    odd = True

    for i in list_of_points:
        if not (-i[0], i[1]) in list_of_points:
            even = False

        if not (-i[0], -i[1]) in list_of_points:
            odd = False

    if even:
        return "Even"
    elif odd:
        return "Odd"
    elif not even and not odd:
        return "Neither even nor odd"


print(function_identifier([(-1, 1), (0, 0), (1, 1)]))


# Medium tasks

def injective_function_validator(list_of_pairs):
    f_range = [i[1] for i in list_of_pairs]
    if len(set(f_range)) != len(f_range):
        return False
    return True


print(injective_function_validator([(2, 4), (3, 6), (4, 8)]))


def surjective_function_checker(function_pairs, codomain):
    f_codomain = [i[1] for i in function_pairs]
    if f_codomain == codomain:
        return True
    return False


print(surjective_function_checker([(1, 2), (2, 3), (3, 4)], [2, 3, 4]))


# Hard tasks

def function_combination_tool(f, g, operation, value):
    operations = {"Addition": "+", "Subtraction": "-", "Multiplication": "*", "Division": "/"}
    x = sympy.symbols("x")
    equation = sympy.sympify(f"({f}) {operations[operation]} ({g})")
    result = equation.subs(x, value)
    return result


print(function_combination_tool("x**2", "2*x + 1", "Addition", 3))
print(function_combination_tool("x**2 + 4 * sqrt(x)", "3", "Division", 9))


def graph_information_extractor(graph_data):
    x_intercepts = []
    y_intercepts = None
    maxima = []
    minima = []

    for i in range(0, len(graph_data) - 1):
        if graph_data[i][0] == 0:
            y_intercepts = graph_data[i][1]
        if graph_data[i][1] == 0:
            x_intercepts.append(graph_data[i][0])
        if i != 0 and graph_data[i - 1][1] < graph_data[i][1] > graph_data[i + 1][1]:
            maxima.append(graph_data[i][1])
        elif i != 0 and graph_data[i - 1][1] > graph_data[i][1] < graph_data[i + 1][1]:
            minima.append(graph_data[i][1])

    return f"""x-intercepts: {None if len(x_intercepts) == 0 else x_intercepts}\ny-intercepts: {y_intercepts}
Maxima: {None if len(maxima) == 0 else maxima}\nMinima: {None if len(minima) == 0 else minima}"""


print(graph_information_extractor([(-2, -4), (-1, -1), (0, 0), (1, 1), (2, 4)]))
print(graph_information_extractor([(-4.5, 0), (-3, 3), (0, 9), (1, 11)]))