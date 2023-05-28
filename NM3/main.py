from matrix import *
from random import randint
from math import sqrt, copysign
from jacobi import *
from random import *
def start():
    N = 30
    epsilon = 1e-9
    eigen_values_corr = generate_X(N)
    x = generate_X(N)
    x.normalize()
    eigen_values_corr.sort()
    print(f'max_eigen_value = {eigen_values_corr.norm()}')

    Diag = make_diag(N, eigen_values_corr)
    E = make_e(N)
    w = Matrix([x])
    wT = w.transpose()
    House = E - wT * w * 2
    HouseT = House.transpose()
    M = House * Diag * HouseT
    [eigen_values_comp, h, it] = solution(M, N, epsilon)
    eigen_values_comp.sort()
    print(f'Iterations = {it}\nError = {(eigen_values_corr - eigen_values_comp).norm()}')

    A_computed = make_diag(N, eigen_values_comp)
    measure_r = (House * A_computed).transpose() - Diag * House
    print(f'r()= {measure_r.norm()}\n\n')
    return


def generate_X(N):
    x = make_vector(N)
    for i in range(1, N + 1):
        x[i] = randint(-50, 50) + round(random(), 3)
        if x[i] == 0: x[i] = 1
    return x

start()