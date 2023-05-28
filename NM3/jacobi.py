from matrix import *
from math import sqrt, copysign


sign = lambda z: copysign(1, z)

def solution(A, N, epsilon):
    # Условия выхода: малость максимального элемента, малость меры A.measure()
    # 1. Найти максимальный i, j элемент A.find_max()
    # 2. p = 2*A[i, j]
    #    q = a[i, i] - a[j, j]
    #    d = sqrt(p^2 + q^2)
    #       1) Если q = 0, c = s = sqrt(2)/2
    #       2) Если q != 0,
    #               r = abs(q)/(2*d),
    #               c = sqrt(0.5 + r)
    #               s = sqrt(0.5 - r)*sign(p*q)
    #    t = s / c
    #    tau = s / (1.0 + c)
    # 3. Изменить A[i, 1..N] A[j, 1..N]
    #             A[1..N, i] A[1..N, j]
    # 4. it++

    e = 1
    it = 0
    [k, l] = A.find_max()
    e = abs(A[k, l])
    h = make_e(N)
    #print(f'Iteration = {it}\n A = \n {A}\n================\n')
    while A.measure() > epsilon:
        p = 2*A[k, l]
        q = A[l, l] - A[k, k]
        d = sqrt(p*p + q*q)

        if q == 0:
            c = sqrt(2)/2
            s = c
        else:
            r = abs(q)/(2*d)
            c = sqrt(0.5 + r)
            s = sqrt(0.5 - r)*sign(p*q)

        t = s / c
        tau = s / (1.0 + c)

        temp = A[k, l]
        A[k, l] = 0.0
        A[l, k] = 0.0
        A[k, k] = A[k, k] - t * temp
        A[l, l] = A[l, l] + t * temp

        for i in range(1, k):  # Case of i < k
            temp = A[i, k]
            A[i, k] = temp - s * (A[i, l] + tau * temp)
            A[i, l] = A[i, l] + s * (temp - tau * A[i, l])
        for i in range(k + 1, l):  # Case of k < i < l
            temp = A[k, i]
            A[k, i] = temp - s * (A[i, l] + tau * A[k, i])
            A[i, l] = A[i, l] + s * (temp - tau * A[i, l])
        for i in range(l + 1, N+1):  # Case of i > l
            temp = A[k, i]
            A[k, i] = temp - s * (A[l, i] + tau * temp)
            A[l, i] = A[l, i] + s * (temp - tau * A[l, i])
        for i in range(1, N+1):  # Update transformation matrix
            temp = h[i, k]
            h[i, k] = temp - s * (h[i, l] + tau * h[i, k])
            h[i, l] = h[i, l] + s * (temp - tau * h[i, l])
        #print(A, '\n')
        [k, l] = A.find_max()
        e = abs(A[k, l])
        it += 1
        #  print(f'Iteration = {it}\n A = \n{A}\n================\n')
    eigen_values = make_vector(N)
    for i in range(1, N+1):
        eigen_values[i] = A[i, i]
    return eigen_values, h, it
