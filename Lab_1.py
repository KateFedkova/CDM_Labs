# Lab 1: "Basic Set Operations"
# Objective: Implement foundational set operations without using pre-built libraries or classes


class Set:

    def __init__(self, elements=None):
        self.created_set = self.create_set(elements)

    def __repr__(self):
        return str(self.created_set)

    @staticmethod
    def create_set(elements):
        new_set = []
        if elements:
            for i in elements:
                if i not in new_set:
                    new_set.append(i)
        return new_set

    def add_element(self, element):
        if element not in self.created_set:
            self.created_set.append(element)
        return self.created_set

    def remove_element(self, element):
        if element in self.created_set:
            self.created_set.remove(element)
        return self.created_set

    def contains_element(self, element):
        return element in self.created_set

    def union(self, set_b):
        new_set = [el for el in self.created_set if el not in set_b] + set_b
        return new_set

    def intersection(self, set_b):
        new_set = [el for el in self.created_set if el in set_b]
        return new_set

    def difference(self, set_b):
        new_set = [el for el in self.created_set if el not in set_b]
        return new_set

    def complement(self, universal_set):
        new_set = [el for el in universal_set if el not in self.created_set]
        return new_set


def first_iteration(expression, dict):
    new_set = []
    action = expression.split()[:3]
    new_expression = expression.split()[3:]
    first_set = Set(dict[action[0]])
    second_set = dict[action[2]]

    if action[1] == "union":
        new_set = first_set.union(second_set)

    elif action[1] == "intersection":
        new_set = first_set.intersection(second_set)

    elif action[1] == "difference":
        new_set = first_set.difference(second_set)

    elif action[1] == "complement":
        new_set = first_set.complement(second_set)

    return new_set, new_expression


def check_expression(expression, sets_dict):
    available_commands = ["union", "intersection", "difference", "complement"] + list(sets_dict.keys())
    for i in expression.split():
        if i not in available_commands:
            return False
    return True


def evaluate_expression(expression, sets_dict):
    if check_expression(expression, sets_dict):
        new_set, new_expression = first_iteration(expression, sets_dict)

        while len(new_expression) >= 2:
            new_action = new_expression[:2]
            if new_action[0] == "union":
                new_set = Set(new_set).union(sets_dict[new_action[1]])

            elif new_action[0] == "intersection":
                new_set = Set(new_set).intersection(sets_dict[new_action[1]])

            elif new_action[0] == "difference":
                new_set = Set(new_set).difference(sets_dict[new_action[1]])

            elif new_action[0] == "complement":
                new_set = Set(new_set).complement(sets_dict[new_action[1]])

            new_expression = new_expression[2:]

        return new_set
    else:
        return "Check your spelling"


# Set Creation

lab_set = Set([1, 2, 2, 3])
print(lab_set)

# Set Manipulation

print(lab_set.add_element(4))
print(lab_set.remove_element(4))
print(lab_set.contains_element(4))

# Advanced Set Operations

print(lab_set.union([3, 4, 5]))
print(lab_set.intersection([3, 4, 5]))
print(lab_set.difference([3, 4, 5]))
print(lab_set.complement([1, 2, 3, 4, 5]))

# Expression Evaluator

expression = "A intersection B union C difference A"
sets_dict = {'A': [1, 2, 3], 'B': [3, 4, 5], 'C': [5, 6, 7]}

print(evaluate_expression(expression, sets_dict))

