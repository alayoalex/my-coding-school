# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def suma(a, b):
    return a + b

def multi(a, b):
    return a*b

funcs = [suma, multi]
print(funcs)
print(funcs[0])
print(funcs[0](2,3))
print(funcs[1](2,3))