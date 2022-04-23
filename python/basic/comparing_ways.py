# "is" vs "=="

a = [1, 2, 3]
b = a

print(a is b)
print(a == b)

print()

c = list(a)   # Now c point to a new objet bult with the object in a.
print(c)
print(type(c))
print(type(a))

print(a == c)  # They keep with the same values. 
print(a is c)  # Now c point to a new objet bult with the object in a.

# • "is" expressions evaluate to True if two variables point to the same object
# • "==" evaluates to True if the objects referred to by the variables are equal