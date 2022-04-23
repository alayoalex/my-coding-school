"""This mechanism is useful for separating concerns and avoiding external unrelated logic 
‘polluting’ the core logic of the function or method. A good example of a piece of functionality 
that is better handled with decoration is memoization or caching: you want to store the results 
of an expensive function in a table and use them directly instead of recomputing them when they
have already been computed. This is clearly not part of the function logic.
"""

# Example 1: Manually decorate, taking ventage from the fact that function are object.
def foo():
    return 5**5

def decorator(func):
    return print(func) # manipulate func

def decorator_1(func):
    return func()

faa = decorator(foo)
print(foo())          # Calling the undecorated function directly
#print(faa())
#print(decorator(foo)())
print(decorator_1(foo))

print()

# Example 2
@decorator
def bar():
    return 5**3
# bar() is decorated

def undec():
    return 3**5

print(bar())
#print(decorator(bar))
#print(decorator_1(bar))

print()

print(decorator(undec))