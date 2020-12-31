def palindrome_1(n):
    """Compare with a pointer from the begining and the end of the string. This can be improved
    stoping when i > len(n/2)"""
    palindrome = True
    for i in range(len(n)):
        if (n[i] != n[len(n)-1-i] and i < len(n)/2):
            palindrome = False
    return palindrome

def palindrome_2(n):
    """buld and inverted string with the original and compare them."""
    n_inverted = ''
    palindrome = True
    for i in range(len(n)):
        n_inverted += n[len(n)-1-i]
    if n != n_inverted:
        palindrome = False
    return palindrome


# tests
print(palindrome_1("asdfdsa"))
print(palindrome_2("asdfdsa"))