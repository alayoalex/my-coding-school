"""This module generates the amount of primes in an interval [2,n].
Two methods are used to it, Gauss Equation and Francis Heuristic
"""

import math

contstand_list = [2.5, 2.6, 2.7, 2.789, 2.851, 2.86, 2.86, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8]
interval = int(math.log10(1000000000000000))

def count_primes_francis(intervalo=100):
    n = int(math.log10(intervalo))    
    results = 2
    for i in range(n-1):
        results *= contstand_list[i]   
    return results**2


def count_primes_gauss(intevalo=100):
    return intevalo/math.log(intevalo)

# tests
print("\nGenerando intervalos hasta 10^" + str(interval))
print("\nEcuación de Gauss: ")
for i in range(1, interval):
    print(str(count_primes_gauss(10**i)), end="\n")

print()


print("Método de Francis: ")
for i in range(len(contstand_list)):
    print(count_primes_francis(10**(i+1)), end="\n")

print("\nGenerando " + str(len(contstand_list)) + " secuencia de numeros: ")