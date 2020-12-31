"""
In 1706 John Machin came up with the first really fast method of calculating π 
and used it to calculate π to 100 decimal places. Quite an achievement considering 
he did that entirely with pencil and paper. Machin's formula is:
    
    π/4 = 4cot⁻¹(5) - cot⁻¹(239)
        = 4tan⁻¹(1/5) - tan⁻¹(1/239)
        = 4 * arctan(1/5) - arctan(1/239)

https://www.craig-wood.com/nick/articles/pi-machin/
http://en.wikipedia.org/wiki/John_Machin
Euler better formula for arctan: http://mathworld.wolfram.com/InverseTangent.html
"""

import math, time


def arctan(x, one=1000000):
    """
    Calculate arctan(1/x)

    arctan(1/x) = 1/x - 1/3*x**3 + 1/5*x**5 - ... (x >= 1)

    This calculates it in fixed point, using the value for one passed in
    """

    power = one // x            # the +/- 1/x**n part of the term
    total = power               # the total so far
    x_squared = x * x           # precalculate x**2
    divisor = 1   
                  # the 1,3,5,7 part of the divisor
    while 1:
        power = - power // x_squared
        divisor += 2
        delta = power // divisor
        if delta == 0:
            break
        total += delta
    return total


def arctan_euler(x, one=1000000):
    """
    Calculate arctan(1/x) using euler's accelerated formula

    This calculates it in fixed point, using the value for one passed in
    """
    x_squared = x * x
    x_squared_plus_1 = x_squared + 1
    term = (x * one) // x_squared_plus_1
    total = term
    two_n = 2
    
    while 1:
        divisor = (two_n+1) * x_squared_plus_1
        term *= two_n
        term = term // divisor
        if term == 0:
            break
        total += term
        two_n += 2
    return total


def pi_machin(one):
    return 4*(4*arctan(5, one) - arctan(239, one))


def pi_ferguson(one):
    return 4*(3*arctan(4, one) + arctan(20, one) + arctan(1985, one))


def pi_hutton(one):
    return 4*(2*arctan(3, one) + arctan(7, one))


def pi_gauss(one):
    return 4*(12*arctan(18, one) + 8*arctan(57, one) - 5*arctan(239, one))


if __name__ == "__main__":
    print(pi_machin(10**100))

    for log10_digits in range(1,7):
        digits = 10**log10_digits
        one = 10**digits

        start = time.time()
        pi = pi_machin(one)
        #print(pi)
        print("Machin: digits", digits, "time", time.time()-start)