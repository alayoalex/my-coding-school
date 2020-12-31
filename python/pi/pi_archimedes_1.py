import math, time


def compute_pi(k):
    incrito, cincunscrito = [],[]

    incrito.append(3.0)
    cincunscrito.append(2.0*math.sqrt(3.0))
    print(f"k=0 ==> 6 Lados >> Defecto: {incrito[0]:2f}, Exceso: {cincunscrito[0]:2f}")
    #n = 6*2**k

    for i in range(1,k+1):
        start = time.time()
        
        n = 6*2**(i)
        aux = 2.0*incrito[i-1]*cincunscrito[i-1]/(incrito[i-1]+cincunscrito[i-1])
        cincunscrito.append(aux)
        incrito.append(math.sqrt(incrito[i-1]*aux))
        
        end = time.time()
        tiempo = end - start
        
        print(f"k={i} ==> {n} Lados >> Defecto: {incrito[i]:2f}, Exceso: {aux:2f}, Tiempo: {tiempo:2f}")


def main():
    n = 20
    compute_pi(n)


if __name__ == "__main__":
    main()