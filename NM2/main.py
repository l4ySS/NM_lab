from test import *
from random import *


def generate_U(N, L, condition='good', k=2):
    U = make_matrix(N, L)
    if condition == 'good':
        for i in range(1, N + 1):
            for j in range(i, U.kN(i) + 1):
                U[i, j - i + 1] = randint(-10, 10) + round(random(), 3)
                if U[i, j - i + 1] == 0: U[i, j - i + 1] = 1
        for i in range(1, N + 1):
            U[i, 1] *= 10**k
    if condition == 'bad':
        for i in range(1, N + 1):
            for j in range(i, U.kN(i) + 1):
                U[i, j - i + 1] = randint(-10, 10) + round(random(), 3)
                if U[i, j - i + 1] == 0: U[i, j - i + 1] = 1
        for i in range(1, N + 1):
            U[i, 1] /= 10**k
    return U


def generate_default(N, L):
    U = make_matrix(N, L)
    for i in range(1, N + 1):
        for j in range(i, U.kN(i) + 1):
            U[i, j - i + 1] = randint(-10, 10) + round(random(), 3)
            if U[i, j - i + 1] == 0: U[i, j - i + 1] = 1
    return U


def generate_X(N):
    x = make_vector(N)
    for i in range(1, N + 1):
        x[i] = randint(-10, 10) + round(random(), 3)
        if x[i] == 0: x[i] = 1
    return x


def start():
    N = 80
    L = 10

    U = generate_U(N, L, condition='good')
    x_corr = generate_X(N)

    A = make_A(U, N, L)
    [f, y] = make_solution(U, x_corr, N, L)
    print(f'y = {f}')
    x_comp = solution(A, N, L, f)
    print(f'Error = {(x_corr - x_comp).norm()}')
    return


start()