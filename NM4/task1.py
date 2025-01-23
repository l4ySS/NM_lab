import numpy as np
import matplotlib.pyplot as plt
from array import *


def f(x):
    return 0.5*x**2 - 3*x + 0.2
    # exp(0.05*x)+4
    # 1/(1+25*x**2)
    # abs(x)
    # 0.1 * x**7 + 1 * x**6 - 3.4 * x**5 + 12 * x**4 - 2.3 * x**3 - x**2 + 400 * x - 20
    # 0.5*x**2 - 3*x + 0.2
    # sin(x)
    # 6*x**3-x**2-9*x+10
    # -4*x**6+5*x**5-1*x**4+2*x**3+5*x**2+10*x+3
    # 75 + 197 / 2 * (x - 2.5) + 44 * (x - 2.5) ** 2 + 6 * (x - 2.5) ** 3
    # 36+59 * (x-2) + 35 * (x-2)**2 + 388/18 * (x-2)**3
    # 14.5+241/6 * (x-1.5) + 8/3 * (x-1.5)**2 - 524/6 * (x-1.5)**3
    # 2*x + 6/x +3


def uniform_partition(n, a, b):
    x = array('d')
    for i in range(n):
        x.append(a + ((b - a) / n) * i)
    return x


def chebyshev_partition(n, a, b):
    x = array('d')
    for i in range(n):
        x.append((a + b) / 2 - ((b - a) / 2) * np.cos(((2 * i + 1) / (2 * n + 1)) * np.pi))
    return x


def l(i, n, x, x_curr):
    num = 1
    denum = 1
    for j in range(n):
        if j == i:
            continue
        num *= (x_curr-x[j])
        denum *= (x[i]-x[j])
    return num / denum


def lagrange(j, n, x, y, x_curr):
    p = 0
    for i in range(j, n):
        p += y[i]*l(i, n, x, x_curr)
    return p


def start_task1(partition, n, draw='false'):
    a = -1
    b = 1
    y = []
    error = []
    h = []
    polynom = []

    x = partition(n, a, b)
    for i in range(n):
        y.append(f(x[i]))
    for i in range(n - 1):
        h.append(x[i + 1] - x[i])

    for i in range(n - 1):
        polynom.append(lagrange(0, n, x, y, x[i] + h[i] / 2))
    for i in range(n - 1):
        error.append(abs(f(x[i] + h[i] / 2) - polynom[i]))
    print(f'{partition.__name__}    \t|\t{n}\t|\t MaxError() = {max(error)}')
    x_prom = []
    p = []
    for i in range(n - 1):
        x_prom.append(x[i] + h[i] / 2)
        p.append(polynom[i])

    x_real, y_real = [[], []]
    j = 0
    for k in np.arange(a, b, 0.0001):
        x_real.append(k)
        y_real.append(f(x_real[j]))
        j += 1

    if draw == 'true':
        name = 'Равномерное разбиение' if partition.__name__ == 'uniform_partition' else 'Разбиение Чебышева'
        plt.figure()
        plt.title(name)
        plt.plot(x_real, y_real, label='f(x)')
        plt.plot(x, y, 'ro')
        plt.plot(x_prom, p, label='Pn(x)')
        plt.legend()
        plt.grid()
        plt.figure()
        plt.title(name)
        i = list(range(error.__len__()))
        plt.plot(i, error)
        plt.grid()
        plt.draw()
        plt.show()


#n = [6, 12]
#for i in n:
##   start_task1(uniform_partition, i, 'true')
#   start_task1(chebyshev_partition, i, 'true')


