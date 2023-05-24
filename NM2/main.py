from test import *
from random import *


def generate_U(N, L):
    U = make_matrix(N, L)
    for i in range(1, N + 1):
        for j in range(i, U.kN(i) + 1):
            U[i, j - i + 1] = randint(-10, 10) + round(random(), 3)
            if U[i, j - i + 1] == 0: U[i, j - i + 1] = 1

    return U


def generate_X(N):
    x = make_vector(N)
    for i in range(1, N + 1):
        x[i] = randint(1, 10)
        if x[i] == 0: x[i] = 1
    return x


def start():
    N = 40
    L = 4

    U = generate_U(N, L)
    x_corr = generate_X(N)

    A = make_A(U, N, L)
    [f, y] = make_solution(U, x_corr, N, L)
    print(f'y = {y}')
    print((x_corr - solution(A, N, L, f)).norm())
    return


start()