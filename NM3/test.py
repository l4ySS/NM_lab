from matrix import *
from jacobi import *
import sys

def run():
    x1 = Vector([9, 0, 0, 6, 1])
    x2 = Vector([0, -5, 0, -8, 8])
    x3 = Vector([0, 0, -6, -2, 7])
    x4 = Vector([6, -8, -2, -5, 6])
    x5 = Vector([1, 8, 7, 6, -8])

    M = Matrix([x1, x2, x3, x4, x5])

    print('This message will be displayed on the screen.')
    with open('matrix.txt', 'w') as f:
        for i in range(1, 6):
            for j in range(1, 6):
                print(M[i, j], end=' ', file=f)
            print('\n', file=f)
    print(f'M = \n{M}')
    [eigenvalues, h, it] = solution(M, 5, 1e-32)
    print(f'\niterations = {it}\neigenvalues = \n{eigenvalues}\n\nH=\n{h}')

run()
