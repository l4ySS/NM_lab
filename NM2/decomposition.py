from matrix import *
from vector import *
from cmath import sqrt


def make_solution(U, x, N, L):
    # Умножение U*x = y
    y = make_vector(N)
    sum = 0
    for i in range(1, N + 1):
        for j in range(i, U.kN(i) + 1):
            sum += U[i, j - i + 1] * x[j]
        y[i] = sum
        sum = 0
    #   print(f'y = {y}')

    # Умножение L*y = f
    f = make_vector(N)
    sum = 0
    for i in range(1, N + 1):
        for j in range(U.k0(i), i+1):
            sum += U[j, (i - j) + 1] * y[j]
        # sum += y[i]
        f[i] = sum
        sum = 0
    return f, y


def make_A(U, N, L):
    scal = 0
    result = make_matrix(N, L)
    for i in range(1, N + 1):
        for j in range(U.k0(i), i + 1):
            for k in range(U.k0(i), j + 1):
                scal += U[k, (i - k) + 1] * U[k, (j - k) + 1]
            result[i, (j - i) + L] = scal
            scal = 0
    return result


def solution(A=Matrix(), N=0, L=0, f=Vector([])):
    # print(f'A = \n{A}')
    #print(f'f = {f}')
    U = make_matrix(N, L)

    for i in range(1, N + 1):
        s = A[i, A.L]

        for k in range(A.k0(i), i):
            s = s - U[k, i - k + 1] * U[k, i - k + 1]
        U[i, 1] = sqrt(s)

        for j in range(i + 1, A.kN(i) + 1):
            s = A[j, A.L + i - j]
            for k in range(A.k0(j), i):
                s = s - U[k, i - k + 1] * U[k, j - k + 1]
            U[i, j - i + 1] = s / U[i, 1]

    #print(U)

    y = make_vector(A.N)
    for i in range(1, A.N + 1):
        s = f[i]
        for j in range(A.k0(i), i):
            s = s - U[j, (i - j) + 1] * y[j]
        y[i] = s / U[i, 1]
    #print(f'y = {y}')

    x = make_vector(A.N)
    for i in range(A.N, 0, -1):
        s = y[i]
        for j in range(i + 1, A.kN(i) + 1):
            s = s - U[i, j - i + 1] * x[j]
        x[i] = s / U[i, 1]

    return x
