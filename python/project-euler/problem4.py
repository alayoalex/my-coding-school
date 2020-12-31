def palindrome_1(n):
    """Compare with a pointer from the begining and the end of the string. 
    This can be improved stoping when i > len(n/2)"""
    palindrome = True
    for i in range(len(n)):
        if (n[i] != n[len(n)-1-i] and i < len(n)/2):
            palindrome = False
    return palindrome

li = []
for i in range(100,1000):
    for j in range(100,1000):
        if palindrome_1(str(i*j)):
            li.append(i*j)

li.sort()
print(li[-1])
