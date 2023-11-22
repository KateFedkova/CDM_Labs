# Lab 4: Number Theory and Functions

import sympy
from sympy.calculus.util import continuous_domain, function_range


# Easy tasks

def parity_checker(number):
    return "Even" if number % 2 == 0 else "Odd"


print(parity_checker(25))


def prime_number_checker(number):
    if number == 1 or number == 0:
        return "Not prime"
    for i in range(2, number):
        if number % i == 0:
            return "Not prime"
    return "Prime"


print(prime_number_checker(17))


def gcd_calculator(num1, num2):
    if num1 % num2 == 0:
        return num2
    return gcd_calculator(num2, num1 % num2)


print(gcd_calculator(48, 18))

# Medium Tasks


def how_many_times_divides(number, divisor, factors):
    while number % divisor == 0:
        if divisor not in factors:
            factors[divisor] = 1
        else:
            factors[divisor] += 1
        number /= divisor
    return factors, number


def form_result(factors):
    result = ""
    list_of_factors = [key for key, value in factors.items()]
    last_factor = list_of_factors[len(list_of_factors) - 1]
    for key, value in factors.items():
        if key == last_factor and value == 1:
            result += f"{key}"
        elif key == last_factor:
            result += f"{key}^{value}"
        elif value == 1:
            result += f"{key} * "
        else:
            result += f"{key}^{value} * "
    return result


def prime_factorization(number):
    factors, number = how_many_times_divides(number, 2, {})
    factors, number = how_many_times_divides(number, 3, factors)

    divisor = 5
    while divisor <= number:
        factors, number = how_many_times_divides(number, divisor, factors)
        divisor += 2

    return form_result(factors)


print(prime_factorization(56))


def lcm_calculator(num1, num2):
    return int(num1 * num2 / gcd_calculator(num1, num2))


print(lcm_calculator(15, 20))


def direct_proof_method(number):
    proof = f"Step 1: Let n be an even number \n" \
            f"Step 2: By definition, an even number can be expressed as 2k for some integer k \n" \
            f"Step 3: As it can be expressed as 2k, it is divisible by 2 \n" \
            f"Conclusion: if n is an even number, then it is divisible by 2 \n"
    if parity_checker(number) == "Even":
        proof += f"This statements is true for {number} as it is even"
    else:
        proof += f"This statements isn't true for {number}, as it is odd"

    return proof


print(direct_proof_method(6))

# Hard tasks


def eulers_totient_function(number):
    quanity = 0
    if prime_number_checker(number) == "Prime":
        return number - 1

    for i in range(1, number + 1):
        if gcd_calculator(i, number) == 1:
            quanity += 1
    return quanity


print(eulers_totient_function(12))


def square_number(num):
    return num ** 2


def find_odd_sum(num):
    sum = 0
    for i in range(1, num * 2, 2):
        sum += i
    return sum


def proof_by_induction(n):
    proof = f"Suppose that the sum of the first n odd numbers is n^2 for all positive integers \n"
    if square_number(1) == 1:
        proof += f"Basic step: when n = 1, the sum of the first n odd numbers is simply 1^2 = 1, which is true \n"
    else:
        proof += f"Basic step when n = 1 failed, because 1^2 != {square_number(1)}"
        return proof

    proof += f"Induction hypothesis: Assume that the sum of the first k odd numbers is k^2 \n" \
             f"Let's check this for k = {n} \n"

    sum1 = find_odd_sum(n)
    if sum1 == square_number(n):
        proof += f"As {n}^2 = {sum1}, the induction hypothesis is true. Now let's check it for n = k + 1 \n"
    else:
        proof += f"Induction hypothesis when k = {n} failed, because {n}^2 != {sum1}"
        return proof

    sum2 = find_odd_sum(n+1)
    if sum2 == square_number(n + 1):
        proof += f"As {n + 1}^2 = {sum2}, this statement is true for all the positive integers"
    else:
        proof += f"{n + 1}^2 != {sum2}. So, statement isn't true for all the positive integers"
        return proof
    return proof


print(proof_by_induction(5))


def evaluate_function(function, value):
    x = sympy.symbols('x')
    equation = sympy.sympify(function)
    result = equation.subs(x, value)
    domain = continuous_domain(equation, x, sympy.S.Reals)
    f_range = function_range(equation, x, domain)
    return f"f({value}) = {result}\nDomain of the function: {domain} \nRange of the function: {f_range}"


print(evaluate_function("x**2 + 2*x + 1", 3))