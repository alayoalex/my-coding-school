"""
Pi computing using Gregory's series (or sometimes the Leibnitz formula) for π.
This may be the simplest infinite series formula for π but it has the disadvantage
that you'll need to add up a great number of terms to get an acceptably accurate answer.

https://www.craig-wood.com/nick/articles/pi-gregorys-series/
http://mathworld.wolfram.com/GregorySeries.html
http://mathworld.wolfram.com/LeibnizSeries.html
http://www.math.wpi.edu/IQP/BVCalcHist/calc3.html
Trascendentes Tempranas. Stewart. Tomo II. epig-11.9. Ejemplo 7.
History of the formulas and calculations for pi. Jesus Aguilera. p3. 

You can also see something very odd in the error terms - the result is 
correct to 10 decimal places, all except for one digit. This is a known 
oddity and you can read up about it in: http://en.wikipedia.org/wiki/Leibniz_formula_for_pi
"""

import math, time


def pi_gregory(n):
    """
    Calculate n iterations of Gregory's series
    """
    result = 0
    divisor = 1
    sign = 1
    for i in range(n):
        result += sign / divisor
        divisor += 2
        sign = -sign
    return 4 * result

def main():
    """
    Try Gregory's series
    """
    for log_n in range(1,8):
        n = 10**log_n
        start = time.time()
        result = pi_gregory(n)
        end = time.time()
        tiempo = end - start
        error = result - math.pi
        print("%8d iterations %.10f error %.10f tiempo %.10f seg" % (n, result, error, tiempo))


if __name__ == "__main__":
    main()