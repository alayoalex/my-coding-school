class MyClass:
    """A simple class example."""
    i = 12345

    def f(self):
        return 'Hello World'

    def __init__(self):
        self.data = []


class Complex:
    def __init__(self, realpart, complexpart):
        self.i = complexpart
        self.r = realpart


print(MyClass.i)
print(MyClass.f)
print(MyClass.__doc__)

x =  MyClass()
print(x)

c = Complex(3.0, -4.0)
print(c.r, ' ', c.i)