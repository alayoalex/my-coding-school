import math, time


def is_prime(n):
    """
    Valida si un número n es primo o no.
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def list_primes(n):
    """
    Lista todos los números primos entre 2 y un número n.
    Hace uso de la función is_prime().
    """
    l = [2]
    for i in range(3, n, 2):
        if is_prime(i):
            l.append(i)
    return l


def list_primes_otro(n):
    """
    Otra implementación con todo incluido sin llamar a la función is_prime().
    Retorna una lista con todos los numeros primos en el intervalo [2,n].
    Realiza una busqueda ingenua entre 2 y la raiz del numero que se esta comprobando.
    """
    p = [2]
    for j in range(3,n,2):
        primo = True
        for i in range(2, int(math.sqrt(j)) + 1):
            if j % i == 0:
                primo = False
                break
        if primo:
            p.append(j)
    return p


def list_primes_optimized(n):
    """
    TODO: Revisar la optimización.
    Este algoritmo supuestamente optimizado funciona mas lentamente que el otro.
    Retorna una lista con todos los numeros primos en el intervalo [2,n].
    Realiza una busqueda ingenua entre 2 y la raiz del numero que se esta comprobando.
    """
    p = [2]
    P = 1
    for i in range(3,n,2):
        isp = True
        for j in range(int(math.sqrt(i)) + 1):
            if isp and j < P and p[j]**2 <= i:
                if i % p[j] == 0:
                    isp = False
                    break
        if isp: 
            p.append(i)
            P += 1
    return p


def list_primes_criba_eratostenes(n):
    """
    Criba de Eratostenes, algoritmos mucho más óptimo que los anteriores.
    Consiste en ir tachando en una lista de números naturales, todos los múltiplos de los
    primos que vamos encontrando, hasta quedarnos solo con los primos.
    """
    isprimo = [True for x in range(n)]

    for i in range(2,n):
        if isprimo[i]:
            for j in range(2*i, n, i):
                isprimo[j] = False
        
    l = [x for x in range(2,n) if isprimo[x] == True]
    return l


# tests
start = time.time()
print(is_prime(67280421310721))
end = time.time()
print(end - start)

#print()

#start1 = time.time()
#print("Normal: " + str(list_primes(10000)))
#print(len(list_primes(10000)))
#end1 = time.time()

#print()

#start2 = time.time()
#print("Optimazado: " + str(list_primes_optimized(10000)))
#print(len(list_primes_optimized(10000)))
#end2 = time.time()

#print()

#start3 = time.time()
#print("Criba: " + str(list_primes_criba_eratostenes(10000)))
#print(len(list_primes_criba_eratostenes(10000)))
#end3 = time.time()

#print()

#start4 = time.time()
#print("Otro: " + str(list_primes_otro(10000)))
#print(len(list_primes_criba_eratostenes(10000)))
#end4 = time.time()

#print()

#print("Normal " + str(end1 - start1))
#print("Optimizado: " + str(end2 - start2))
#print("Criba: " + str(end3 - start3))
#print("Otro: " + str(end4 - start4))