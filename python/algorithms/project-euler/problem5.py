divisible = False
number = 10

while not divisible:
    number += 1
    for i in range(2,20):
        if number % i != 0:
            break
    else:
        divisible = True
        break

print(number)
