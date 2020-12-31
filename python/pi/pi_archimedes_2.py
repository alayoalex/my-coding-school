"""
Draw a circle of radius 1 unit centered at A. 
Inscribe an N sided polygon within it. 
Our estimate for π is half the circumference of the polygon 
(circumference of a circle is 2πr, r = 1, giving 2π). 
As the sides of the polygon get smaller and smaller the 
circumference gets closer and closer to 2π.

Hooray! We calculated π to 8 decimal places in only 13 iterations.
Iteration 0 for the square shows up the expected 2.828 estimate for π.
You can see after iteration 13 that the estimate of π starts getting worse. 
That is because we only calculated all our calculations to the limit 
of precision of python's floating point numbers (about 17 digits), 
and all those errors start adding up.

https://www.craig-wood.com/nick/articles/pi-archimedes/
"""

import math, time


def pi_archimedes(n):
    """
    Calculate n iterations of Archimedes PI recurrence relation
    """
    polygon_edge_length_squared = 2.0
    polygon_sides = 4
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * math.sqrt(1 - polygon_edge_length_squared / 4)
        polygon_sides *= 2
    return polygon_sides * math.sqrt(polygon_edge_length_squared) / 2


def main():
    """
    Try the series
    """
    for n in range(16):
        start = time.time()
        result = pi_archimedes(n)
        end = time.time()
        tiempo = end - start
        error = result - math.pi
        print("%8d iterations %.10f error %.10f tiempo %.10f seg" % (n, result, error, tiempo))



if __name__ == "__main__":
    main()
