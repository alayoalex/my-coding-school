import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2 - 2*x - 2


def biseccion(a, b, epsilon):
    c = (a + b) / 2.0
    while f(c) != 0 and b - a > epsilon:
        if f(a)*f(c) > 0:
            a = c
        elif f(b)*f(c) > 0:
            b = c
        c = (a + b) / 2.0
    return c


result = biseccion(0.5, 3.5, 1e-10)
fresult = f(result)

print(f"x = {result:.3f}")

x = np.linspace(0.5, 3.5, 100)
fx = f(x)

plt.plot(x, fx)
plt.plot(result, fresult, 'bs')
plt.show()