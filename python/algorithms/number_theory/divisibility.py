"""
Some of these algorithms are from the book: 
[1] Discrete Mathematics and Its Applications. by Kenneth H. Rosen
"""

import math

def divide_to(a,b):
    """
    Function that verify if a number a divide another number b. 
    Theorem: If a and b are integers with a != 0, we say that a divides b 
    if there is an integer c such that b = ac, or equivalently, 
    if b/a is an integer. When a divides b we say that a is a factor or divisor
    of b, and that b is a multiple of a. The notation a|b denotes that a divides b. 
    [1] p238
    """
    if a == 0:
        print("No está permitido dividir por cero.")
    elif type(a) != int or type(b) != int:
        print("Los numeros deben ser enteros.")
    else:
        return b % a == 0


def congruent_to(a,b,m):
    """
    Verify if two number are congruent module m.
    - Theorem: Let m be a positive integer. The integers a and b are congruent 
    modulo m if and only if there is an integer k such that a = b + km. [1] p241
    - Definition: If a and b are integers and m is a positive integer, 
    then a is congruent to b modulo m if m divides a − b. We use the notation a ≡ b (mod m) 
    to indicate that a is congruent to b modulo m. We say that a ≡ b (mod m) is a congruence 
    and that m is its modulus (plural moduli). 
    [1] p240
    """
    if m < 1: 
        print("El numero m debe ser positivo")
    elif type(m) != int or type(a) != int or type(b) != int:
        print("Los tres numeros deben ser enteros")
    else: return (a - b) % m == 0


def congruent_to_another(a,b,m):
    """
    Verify if two number are congruent module m.
    Theorem: Let a and b be integers, and let m be a positive integer. Then a ≡ b (mod m) if and only
    if a mod m = b mod m. [1] p241
    """
    if m < 1: 
        print("El numero m debe ser positivo")
    elif type(m) != int or type(a) != int or type(b) != int:
        print("Los tres numeros deben ser enteros")
    else: return a % m == b % m


# TODO: Greather Common Divider.
def gcd(a,b):
    pass


# TODO: Minimal Common Multiplier
def mcm(a,b):
    pass


# TODO: Remainder Chinese Theorem
def chinese(a, m, n):
    pass


# TODO: Linear congruence
def linear_congruences(a, m, n):
    pass


# TODO: Prime generator
def prime_generator(p, n):
    pass
