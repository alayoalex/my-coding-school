a,b=1,2
suma = 0
while b <= 4000000:
    if b%2==0:
        suma += b
    a,b=b,a+b

print(suma)