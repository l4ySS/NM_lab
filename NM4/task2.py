from task1 import lagrange, uniform_partition
import math
import random
import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return 0.1 * x**7 + 1 * x**6 - 3.4 * x**5 + 12 * x**4 - 2.3 * x**3 - x**2 + 400 * x - 20


corr1 = [0.1, 1, -3.4, 12, -2.3, -1, 400, -20]


def f2(x):
    return 0.002*x + 6.7321/x + 3.333


corr2 = [0.002, 6.7321, 3.333]


def fi1(sol, x):
    return sol[0] * x ** 7 + sol[1] * x ** 6 + sol[2] * x ** 5 + sol[3] * x ** 4 + sol[4] * x ** 3 + sol[5] * x ** 2 + sol[
        6] * x + sol[7]


def fi2(sol, x):
    return sol[0] * x + sol[1] / x + sol[2]


def upl(x, y, n, h, m, k):
    xnew = []
    ynew = []
    t = h[0] / k
    i = 0
    xnew.append(x[0])
    ynew.append(y[0])
    while i < m / 2:
        while xnew[-1] + t <= x[i + 1]:
            xnew.append(xnew[-1] + t)
            ynew.append(lagrange(0, m, x, y, xnew[-1]))
        i += 1

    while i + m / 2 < n - 1:
        while xnew[-1] + t <= x[i + 1]:
            xnew.append(xnew[-1] + t)
            ynew.append(lagrange(math.ceil(i - m / 2), math.ceil(i + m / 2), x, y, xnew[-1]))
        i += 1

    while i < n - 1:
        while xnew[-1] + t <= x[i + 1]:
            xnew.append(xnew[-1] + t)
            ynew.append(lagrange(n - m, n-1, x, y, xnew[-1]))
        i += 1

    for i in range(n):
        x.pop()
        y.pop()
    for i in range(len(xnew)):
        x.append(xnew[i])
        y.append(ynew[i])
    return len(xnew)-1


def solve(m, right, power):
    for i in range(power + 1):
        R = 1 / m[i][i]
        right[i] *= R
        m[i][i] = 1
        for j in range(i + 1, power + 1):
            m[i][j] *= R
        for j in range(i + 1, power + 1):
            right[j] -= right[i] * m[j][i]
            coeff = m[j][i]
            for k in range(i, power + 1):
                m[j][k] -= coeff * m[i][k]

    for i in range(power, -1, -1):
        for j in range(i):
            right[j] -= right[i] * m[j][i]
            m[j][i] -= m[j][i]

    return right


def sfi1(x, y, n, power=7):
    right = []
    m = []
    for i in range(power, -1, -1):
        xKoeff = [0] * (power + 1)
        rPart = 0
        for j in range(n):
            rPart += y[j] * x[j] ** i
            for k in range(power, -1, -1):
                xKoeff[power - k] += x[j] ** k * x[j] ** i
        right.append(rPart)
        m.append(xKoeff)
    right = solve(m, right, power)
    return m, right


def sfi2(x, y, n):
    right = [0] * 3
    M1 = [[0], [0], [0]]
    for i in range(3):
        xKoeff = []
        rPart = 0
        for l in range(3):
            xKoeff.append(0)
        for j in range(n):
            rPart += -2 * y[j] * x[j] ** (i - 1)
            xKoeff[0] += 2 * x[j] * x[j] ** (i - 1)
            xKoeff[1] += 2 * x[j] ** (-1) * x[j] ** (i - 1)
            xKoeff[2] += 2 * x[j] ** (i - 1)
        if (i == 0):
            right[1] = (-1) * rPart
            M1[1] = xKoeff
        if (i == 1):
            right[2] = (-1) * rPart
            M1[2] = xKoeff
        if (i == 2):
            right[0] = (-1) * rPart
            M1[0] = xKoeff
    print(M1)
    solve(M1, right, 2)
    return M1, right


def approx_error(sol, y1, n):
    sum = 0
    for i in range(n):
        sum += (sol[i] - y1[i]) ** 2
    return sum


def approx_error_abs(sol, y1, n):
    max = (sol[0] - y1[0]) ** 2
    for i in range(n):
        if (sol[i] - y1[i]) ** 2 > max:
            max = (sol[i] - y1[i]) ** 2
    return max


def start_task2(n, segment, conditions):
    [f, fi, sfi, corr] = conditions
    a, b = segment
    m = 3
    k = 3
    y = []
    y_new = []
    h = []

    x = uniform_partition(n, a, b)

    for i in range(n):
        y.append(f(x[i]))
    for i in range(n - 1):
        h.append(x[i + 1] - x[i])

    #n = upl(x, y, n, h, m, k)

    d = 0.2*max(y)
    for i in range(n):
        delta = random.uniform(-d / 2, d / 2)
        y_new.append(y[i] + delta)


    m1, right = sfi(x, y, n)
    print('right = ', right)

    x_real, y_real, y_comp = [[], [], []]
    j = 0
    for k in np.arange(a, b, 0.0001):
        x_real.append(k)
        y_real.append(f(x_real[j]))
        j += 1
    j = 0
    for k in np.arange(a, b, 0.0001):
        y_comp.append(fi(right, x_real[j]))
        j += 1
    plt.plot(x_real, y_real, label='real f(x)')
    plt.plot(x, y, 'ro', label='table f(x)')
    plt.grid(True)
    y_solved = []
    for xr in x:
        y_solved.append(fi(right, xr))

    error = []
    for i in range(len(right)):
        print(i)
        error.append(abs(corr[i]-right[i]))

    print("Error(^2) = ", str(approx_error_abs(y_comp, y_real, j)))
    print("Error(c-y) = ", max(error))
    plt.plot(x_real, y_comp, label='fi(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

n = 10
a = -2
b = 2
start_task2(n, [a, b], [f1, fi1, sfi1, corr1])
