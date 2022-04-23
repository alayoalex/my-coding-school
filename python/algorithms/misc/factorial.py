import math

# recursive factorial
# TODO: Review the fact that there isn't going deep that factorial of 1000
def rfactorial(n):
    if n == 1 or n == 0:
        return 1
    return n * rfactorial(n - 1)

# iterative factorial
def ifactorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact

# testing
print(rfactorial(5))
print(ifactorial(5))

# using std function
print(math.factorial(1000))