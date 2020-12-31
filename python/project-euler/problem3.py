import math

def esprimo(n):
    if n%2==0 or n%3==0:
        return False
    for i in range(5,math.ceil(math.sqrt(n)),2):
        if n%i == 0:
            return False
    return True

for i in range(math.ceil(math.sqrt(600851475143)),2,-2):
    if esprimo(i) and 600851475143%i==0:
        print(i)