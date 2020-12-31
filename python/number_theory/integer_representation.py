base_16_digits = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}


def base_converter(n, base=2):
    """
    Constructing Base b Expansions from base 10.
    n: is in base 10.
    base: is the new base to generate.

    TODO: Validate base 16 letters (A,B,C,D,E,F)
    """
    q, k = n, 0
    ak = []
    if base < 1:
        print("El numero debe ser positivo.")
    elif type(base) != int:
        print("El numero debe ser entero.")
    else:
        while q != 0:
            ak.append(q % base)
            q = q // base
            k += 1
        ak.reverse()
        numero_converted = ''
        for i in range(len(ak)):
            numero_converted += str(ak[i])
        return numero_converted


def to_decimal_base(n, base):
    """
    base: base of n.
    n: number to convert.
    """
    cadena_de_cifras = str(n)
    result = 0

    if base <= 10:
        for i in range(len(cadena_de_cifras)):
            result += int(cadena_de_cifras[i])*(10**(len(cadena_de_cifras)-i))
    elif base == 16:
        for i in range(len(cadena_de_cifras)):
            if cadena_de_cifras[i] in ['A', 'B', 'C', 'D', 'E', 'F']:
                result = result + base_16_digits[int(cadena_de_cifras[i])]*(10**(len(cadena_de_cifras)-i))
            result = result + int(cadena_de_cifras[i])*(10**(len(cadena_de_cifras)-i))
    else: 
        return print("No esta implementada la funcionalidad para otras bases mayores que 10.")
    return result


def from_oct_to_bin(n):
    numero = n
    lista_cifras = []
    numero_binario = ''

    while numero != 0:
        lista_cifras.append(numero % 10)
        numero = numero // 10
    lista_cifras.reverse()
    
    binaria = ''
    for i in lista_cifras:
        binaria += base_converter(i, 2)
    return binaria
        

# TODO
def from_hex_to_bin(n):
    pass


# TODO
def from_bin_to_oct(n):
    pass


# TODO
def from_bin_to_hex(n):
    pass


# Tests
#print(base_converter(1023, base=2))