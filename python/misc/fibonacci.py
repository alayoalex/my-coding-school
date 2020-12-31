def fib_elements(n):
    """Calcula los elementos de la sucesion de Fibonacci hasta 
    un número n y los imprime separados por un espacio."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

def fib_list(n):
    """Calcula la sucesion de Fibonacci y los almacena en una lista, 
    luego retorna la lista."""
    a, b = 0, 1
    sequence = []
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# tests
print(fib_elements.__doc__)
print(fib_elements(2000))
print(fib_list.__doc__)
print(fib_list(2000))