import math
import random
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from math import *
from array import *


def f(x):
    return x ** 3 - 2 * x ** 2 - 8 * x + 4
    # 1/(1+25*x**2)
    # exp(0.05*x)+4
    # abs(x)
    # 0.01*x**6-3*x**5+12*x**4-2.3*x**3-x**2+4*x-20
    # 0.5*x**2 - 3*x + 0.2
    # sin(x)
    # 6*x**3-x**2-9*x+10
    # 2*x + 6/x +3
    # -4*x**6+5*x**5-1*x**4+2*x**3+5*x**2+10*x+3
    # 10*x**7+0.1*x**6-3*x**5+12*x**4-2.3*x**3-x**2+4*x-20


def fRebuilt(y, x, n):
    for i in range(n + 1):
        y.append(f(x[i]))


def uniformPartition(x, n, a, b):
    h = []
    for i in range(n + 1):
        x.append(a + ((b - a) / n) * i)
        if i > 0:
            h.append(x[i] - x[i - 1])
    return h


def chebyshevPartition(x, n, a, b):
    h = []
    for i in range(n + 1):
        x.append((a + b) / 2 - ((b - a) / 2) * np.cos(((2 * i + 1) / (2 * (n + 1))) * np.pi))
        if i > 0:
            h.append(x[i] - x[i - 1])
    return h


def sol(M, right, step):
    for i in range(step + 1):
        R = 1 / M[i][i]
        right[i] *= R
        M[i][i] = 1
        for j in range(i + 1, step + 1):
            M[i][j] *= R
        for j in range(i + 1, step + 1):
            right[j] -= right[i] * M[j][i]
            coeff = M[j][i]
            for k in range(i, step + 1):
                M[j][k] -= coeff * M[i][k]
    # print(M)
    i = step
    while i > 0:
        for j in range(i):
            right[j] -= right[i] * M[j][i]
            M[j][i] -= M[j][i]
        i -= 1


def step(x, n):
    h = []
    for i in range(n):
        h.append(x[i + 1] - x[i])
    return h


def progonka(A_usl, B_usl, n, h, y):
    c = []
    v = []
    xi = []
    koeff = []
    F = []
    v.append(0)
    xi.append(0)
    v.append(0)
    xi.append(0)
    for i in range(n):
        c.append(0)
    c[n - 1] = B_usl
    koeff.append(2 * (h[0] + h[1]) - (1 / 2) * h[0])
    koeff.append(h[1])
    A = []
    A.append(koeff)
    koeff = []
    koeff.append(h[1])
    koeff.append(2 * (h[1] + h[2]))
    A.append(koeff)
    for i in range(1, n):
        F.append(6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]))

    F[0] -= 3 / h[0] * ((y[1] - y[0]) / h[0] - A_usl) * h[0]
    F[1] -= h[n - 1] * c[n - 1]

    v[0] = F[0] / A[0][0]
    xi[0] = -(A[0][1] / A[0][0])
    for i in range(1, n - 2):
        v[i] = (F[i] - A[i][i - 1] * v[i - 1]) / (A[i][i] + A[i][i - 1] * xi[i - 1])
        xi[i] = -(A[i][i + 1] / (A[i][i] + A[i][i - 1] * xi[i - 1]))
    v[n - 2] = F[n - 2] / A[n - 2][n - 2]
    xi[n - 2] = (-A[n - 2][n - 3] / A[n - 2][n - 2])

    c[1] = (v[n - 2] + xi[n - 2] * v[n - 3]) / (1 - xi[n - 2] * xi[n - 3])
    c[0] = v[0] + xi[0] * c[1]

    return c


def interpol(A_usl, c, y, x):
    a = [y[1], y[2], y[3]]
    M1 = [[-1, 1, 0, 0, (x[1] - x[2]) ** 2 * 0.5, 0],
          [0, x[1] - x[2], 0, 0, (x[1] - x[2]) ** 3 * 1 / 6, 0],
          [0, 0, x[2] - x[3], 0, 0, (x[2] - x[3]) ** 3 * 1 / 6],
          [1, 0, 0, (x[0] - x[1]) ** 2 * 1 / 2, 0, 0],
          [0, 0, 0, 0, (x[1] - x[2]), 0],
          [0, 0, 0, 0, 0, (x[2] - x[3])]]
    r = [float(-(x[1] - x[2]) * c[1]), float(a[0] - a[1] - (x[1] - x[2]) ** 2 * c[1] * 0.5),
         float(a[1] - a[2] - (x[2] - x[3]) ** 2 * 0.5 * c[2]), float(A_usl - (x[0] - x[1]) * c[0]), float(c[0] - c[1]),
         float(c[1] - c[2])]
    sol(M1, r, 5)
    print('r = ', r)
    return r


def inter(A_usl, c, y, x, n, h):
    b = [0]*(n)
    d = [0]*(n)
    a = [y[i] for i in range(1, n + 1)]
    for i in range(1, n):
        d[i] = ((c[i] - c[i-1])/h[i])
    d[0] = (c[0] - A_usl)/h[0]
    for i in range(1, n):
        b[i] = ((y[i+1] - y[i])/h[i]) + h[i]*(c[i-1] + 2*c[i])/6
    b[0] = ((y[1] - y[0])/h[0]) + h[0]*(A_usl + 2*c[0])/6
    
    return b, d


def s(a, b, c, d, x, left, right, h):
    i = 0
    while not (left <= x <= right):
        i += 1
        left = right
        right += h[i]
    return a[i] + b[i] * (x - right) + 0.5 * c[i] * (x - right) ** 2 + 1 / 6 * d[i] * (x - right) ** 3


def error3(sRes, fRes, n, error):
    max = -1
    for i in range(n):
        err = abs(fRes[i] - sRes[i])
        error.append(err)
        if max < err:
            max = err
    return max


def task3():
    a = 0
    b = 1.5
    n = 4
    x = array('d')
    y = array('d')
    error = array('d')
    h = uniformPartition(x, n, a, b)
    fRebuilt(y, x, n)

    x_diff = sp.Symbol('x')
    xx = sp.diff(x_diff ** 3 - 2 * x_diff ** 2 - 8 * x_diff + 4, x_diff)
    A_usl = xx.subs({x_diff: x[0]})
    xx = sp.diff(xx, x_diff)
    print(xx)
    B_usl = xx.subs({x_diff: x[n]})
    h = step(x, n)
    print('A_usl = ', A_usl, 'B_usl = ', B_usl)
    c = progonka(A_usl, B_usl, n, h, y)
    print('c = ', c)
    bd = interpol(A_usl, c, y, x)
    bs, d = inter(A_usl, c, y, x, n, h)
    print('bd = ', bd)
    print('b, d', bs, d)
    a_s = [y[i] for i in range(1, n + 1)]

    print('bd = ', bd)
    #bs = []
    #d = []
    #for i in range(3):
        #bs.append(bd[i])
        #d.append(bd[i + 3])
    print('bs = ', bs)
    x_prom = array('d')
    p = array('d')
    s_res = array('d')
    for i in range(n):
        x_prom.append((x[i] + x[i + 1]) / 2)
        p.append(f(x_prom[i]))
        # s_res.append(s(a_s, bs, c, d, x_prom[i]))

    print(x_prom)
    print(p)
    # print(s_res)

    k = 0
    i = []
    for j in x:
        i.append(k)
        k += 1
    i.pop()
    error = []
    # error3(s_res, p, n, error)
    # print(error)
    print('Coeff = ', a_s, bs, c, d)
    # plt.plot(x_prom, p)
    x_real, y_real = [[], []]
    j = 0
    error = []
    
    for k in np.arange(a, b, 0.0001):
        x_real.append(k)
        s_res.append(s(a_s, bs, c, d, x_real[j], a, a+h[0], h))
        y_real.append(f(x_real[j]))
        error.append(abs(y_real[j] - s_res[j]))
        j += 1
    print('error = ', max(error))
    plt.plot(x, y, x, y, 'ro', label='f(x)')
    plt.plot(x_real, s_res, label='spline')
    plt.grid(True)
    plt.legend()
    plt.show()

    # plt.plot(i, error)
    # plt.grid(True)
    # plt.show()


task3()
