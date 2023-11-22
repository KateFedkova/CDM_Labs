# Lab 3: Advanced Propositional Logic and Computational Logic

import itertools
from tabulate import tabulate

# Complex Logical Expressions Evaluation


def expression_evaluator(expression, values):
    expression = expression.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')

    for i in values:
        if i in expression:
            expression = expression.replace(i, values[i])

    return eval(expression)


expression = "(A AND B) OR (NOT C)"
values = {"A": "True", "B": "False", "C": "True"}

print(expression_evaluator(expression, values))


# Automated Truth Table Generation


def form_values_names(expression):
    logical_operators = ['AND', 'OR', 'NOT']
    values_names = expression.replace(")", "").replace("(", "").split()

    for j in logical_operators:
        if j in values_names:
            values_names.remove(j)

    return values_names


def truth_table_logic(expression):
    data = []
    values_names = form_values_names(expression)
    values = [x for x in itertools.product([True, False], repeat=len(values_names))]

    for value in values:
        value_dict = {value_name: str(bool_val) for value_name, bool_val in zip(values_names, value)}
        combinations = [value_dict[value_name] for value_name in values_names]
        result = expression_evaluator(expression, value_dict)
        combinations.append(result)
        data.append(combinations)

    table = generate_truth_table(values_names, expression, data)
    return table


def generate_truth_table(values_names, expression, data):
    values_names.append(str(expression))
    table = tabulate(data, headers=values_names)
    return table


print(truth_table_logic("(A AND B) OR C"))
