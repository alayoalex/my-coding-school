import collections
counts = collections.Counter(['Fred', 'Samantha', 'Jean-Claude', 'Samantha'])
print(counts)

c = collections.Counter('abcdaab')
for letter in 'abcde':
    print(letter,':', c[letter])