# The lambda keyword in Python provides a
# shortcut for declaring small and 
# anonymous functions:
add = lambda x, y: x + y
print(add(5,3))

# You could declare the same add() 
# function with the def keyword:
def add(x,y):
    return x + y
print(add(4,5))

# So what's the big fuss about?
# Lambdas are *function expressions*:
print((lambda x, y: x + y)(5, 6))

# • Lambda functions are single-expression 
# functions that are not necessarily bound
# to a name (they can be anonymous).

# • Lambda functions can't use regular 
# Python statements and always include an
# implicit `return` statement.