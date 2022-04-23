"""
We can easily calculate more digits of π using Pythons excellent decimal module.
This allows you to do arbitrary precision arithmetic on numbers. 
It isn't particularly quick, but it is built in and easy to use.
Let's calculate π to 100 decimal places now.

https://www.craig-wood.com/nick/articles/pi-archimedes/
"""

from decimal import Decimal, getcontext
import math, time


def pi_archimedes(n):
    """
    Calculate n iterations of Archimedes PI recurrence relation
    """
    polygon_edge_length_squared = Decimal(2)
    polygon_sides = 2
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * (1 - polygon_edge_length_squared / 4).sqrt()
        polygon_sides *= 2
    return polygon_sides * polygon_edge_length_squared.sqrt()


def main():
    """
    Try the series
    """
    places = 100
    old_result = None

    start = time.time()
    for n in range(10*places):
        # Do calculations with double precision
        getcontext().prec = 2*places
        result = pi_archimedes(n)
        # Print the result with single precision
        getcontext().prec = places
        result = +result           # do the rounding on result
        
        print("%3d: %s" % (n, result))
        if result == old_result:
            break
        old_result = result
    end = time.time()
    tiempo = end - start
    print("Tiempo: %5f seg" %(tiempo))


if __name__ == "__main__":
    main()