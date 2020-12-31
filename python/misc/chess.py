"""Algorithms related with chess game."""

import math
import time

"""
Algorithm to get the amount of corn to reward the creator of chess.
"""
def chess_regard_iterative():
    """
    The naive approach lead to an iterative solution.
    """
    total = 0
    for i in range(64):
        total += 2**i
    return total

def chess_regard_equation():
    """
    Applying mathematical induction we can prove that:
    1 + 2 + 2^2 + ... + 2^k = 2^(k+1) - 1
    and so avoid iteration.
    """
    return 2**64 - 1

# tests
s1 = time.time()
iterative = chess_regard_iterative()
e1 = time.time()

s2 = time.time()
equation = chess_regard_equation()
e2 = time.time()

print("Iterative :" + str(iterative) + ", Time: " + str(e1 - s1))
print("Iterative :" + str(equation) + ", Time: " + str(e2 - s2))