# Lab 6

# Easy tasks

def reflexivity_checker(given_set, relation):
    for i in given_set:
        if not (i, i) in relation:
            return False
    return True


print((reflexivity_checker({1, 2, 3}, {(1, 1), (2, 2), (3, 3)})))


def symmetry_identifier(relation):
    for i in relation:
        if not (i[1], i[0]) in relation:
            return False
    return True


print(symmetry_identifier({(1, 2), (2, 1), (3, 3)}))


def transitivity_verifier(relation):
    for i in relation:
        for j in relation:
            if i[1] == j[0] and not (i[0], j[1]) in relation:
                return False
    return True


print(transitivity_verifier({(1, 2), (2, 3), (1, 3)}))


# Medium tasks

def equivalence_relation_checker(given_set, relation):
    if reflexivity_checker(given_set, relation) and symmetry_identifier(relation) \
            and transitivity_verifier(relation):
        return True
    return False


print(equivalence_relation_checker({1, 2, 3}, {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)}))


# Hard tasks

def inverse_relation_generator(relation):
    new_relation = set()
    for i in relation:
        new_relation.add((i[1], i[0]))
    return new_relation


print(inverse_relation_generator({(1, 2), (3, 4), (5, 6)}))
