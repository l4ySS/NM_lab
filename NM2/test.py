from decomposition import *


def run():
    print('------TEST STARTED---------')
    v1 = [Vector([-4.0, 2.0, 3.0, 4.0]),
          Vector([1.0, -2.0, 3.0, 4.0]),
          Vector([0.001, 2.2, 3.0, -4.0]),
          Vector([1.256, 2.3, 3.4, -4.0]),
          Vector([0.11, -2.4, 3.0, 4.0]),
          Vector([0.2, -2.0, 3.0, 0]),
          Vector([1.0, 2.0, 0, 0]),
          Vector([-0.1, 0, 0, 0])
          ]
    N = 8
    L = 4
    mu = Matrix(v1)
    print(f'U = \n{mu}')
    A = make_A(mu, N, L)
    print(f'A = \n{A}')
    x = make_vector(N)
    for i in range(1, N + 1):
        x[i] = 1
    x[N] = 4
    [f, y] = make_solution(mu, x, N, L)
    print(f'y = {y}\n\n')
    print(f'f = {f}\n\n')
    print('----Solution----')

    x_comp = solution(A, N, L, f)
    print((x_comp - x).norm())
    print('------TEST ENDED-----------')
