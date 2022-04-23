# Several ways to iterate using for statements

for element in [1, 2, 3]:
    print(element)
print()

for element in (1, 2, 3):
    print(element)
print()

for key in {'one':1, 'two':2}:
    print(key)
print()

for char in "123":
    print(char)
print()

#for line in open("myfile.txt"):
 #   print(line, end='')


# Iterators

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char)
print()


# Generators

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)


# Generator Expressions

s = sum(i*i for i in range(10))                 # sum of squares
print(s)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
ss = sum(x*y for x,y in zip(xvec, yvec))         # dot product
print(ss)

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_table)

print()
data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))

# unique_words = set(word  for line in page  for word in line.split())
# valedictorian = max((student.gpa, student.name) for student in graduates)