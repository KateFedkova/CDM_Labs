# Lab #2: "Cartesian Products and Relations"
# Objective: Understand and implement the Cartesian product of sets and related operations.

# Basic Cartesian Product

def cartesian_product(set_a, set_b):
    product = []
    for i in set_a:
        for j in set_b:
            product.append((i, j))
    return product


print(cartesian_product([1, 2], ['a', 'b']))


# Relation Testing and Advanced Operations

def is_relation_valid(relation, set_a, set_b):
    products = cartesian_product(set_a, set_b)
    for i in relation:
        if i not in products:
            return False
    return True


print(is_relation_valid([(1, 'a'), (2, 'b')], [1, 2], ['a', 'b']))


def find_relations(set_a, relation_func):
    result_set = []
    for i in set_a:
        for j in set_a:
            if relation_func(i, j):
                result_set.append((i, j))
    return result_set


def is_divisible(a, b):
    if a % b == 0 and a != b:
        return True
    return False


print(find_relations([1, 2, 3, 4, 6], is_divisible))


# Advanced Cartesian Product with Filters

def filtered_cartesian_product(set_a, set_b, filter_function):
    result_set = []
    for i in set_a:
        for j in set_b:
            if filter_function(i, j):
                result_set.append((i, j))
    return result_set


def compare_numbers(a, b):
    if a < b:
        return True
    return False


def divisors(a, b):
    if b % a == 0:
        return True
    return False


print(filtered_cartesian_product([1, 2, 3], [3, 4, 5], divisors))