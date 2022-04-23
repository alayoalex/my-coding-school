# Why Python Is Great:
# Function argument unpacking

def myfuncion(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfuncion(1, 0, 1)
myfuncion(*tuple_vec)
myfuncion(**dict_vec)