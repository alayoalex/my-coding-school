def tranpose():
    matrix = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]        
    trans = [[row[i] for row in matrix] for i in range(4)]
    return trans

print(tranpose())

# Otro ejemplo
even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)

