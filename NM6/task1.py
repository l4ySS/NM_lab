from math import exp
import matplotlib.pyplot as plt
import numpy as np



def f_toch_w1(x):
    return  x**2+16/x
    # x**3
    # x**2+16/x
def f_toch_w2(x):
    return 2*x-16/(x**2)
    # 3*x**2
    # 2*x-16/(x**2)

def f(x, w1, w2):
    return (32+2*x**3-w1*w2)/8
    # 6*x
    # (32+2*x**3-w1*w2)/8
def fy(x, w1, w2):
    return w2/8

def fy_d(x, w1, w2):
    return w1/8


def shooting(a, b, alpha, beta, n, tol, max_iter):
    h = (b-a)/(n-1)
    k = 1
    TK = (beta - alpha)/(b - a)
    x = 0

    while k <= max_iter:
        w1 = []
        w2 = []
        x_table = []
        x_table.append(a)
        w1.append(alpha)
        w2.append(TK)
        u1 = 0
        u2 = 1
        for i in range(1, n):
            x = a + (i-1)*h
            
            k11 = h*w2[i-1]
            k12 = h*f(x, w1[i-1], w2[i-1])
            k21 = h*(w2[i-1]+k12/2)
            k22 = h*f(x+h/2, w1[i-1]+k11/2, w2[i-1]+k12/2)
            k31 = h*(w2[i-1]+k22/2)
            k32 = h*f(x+h/2, w1[i-1]+k21/2, w2[i-1]+k22/2)
            k41 = h*(w2[i-1]+k32/2)
            k42 = h*f(x+h, w1[i-1]+k31/2, w2[i-1]+k32)
            w1.append(w1[i-1] + (k11 + 2*k21 + 2*k31 + k41)/6)
            w2.append(w2[i-1] + (k12 + 2*k22 + 2*k32 + k42)/6)

            k11_ = h*u2
            k12_ = h*(fy(x, w1[i-1], w2[i-1])*u1 +
                      fy_d(x, w1[i-1], w2[i-1])*u2)
            k21_ = h*(u2+k12_/2)
            k22_ = h*(fy(x+h/2, w1[i-1], w2[i-1])*(u1+k11_/2) +
                     fy_d(x+h/2, w1[i-1], w2[i-1])*(u2+k12_/2))
            k31_ = h*(u2+k22_/2)
            k32_ = h*(fy(x+h/2, w1[i-1], w2[i-1])*(u1+k21_/2) +
                     fy_d(x+h/2, w1[i-1], w2[i-1])*(u2+k22_/2))
            k41_ = h*(u2+k32_/2)
            k42_ = h*(fy(x+h, w1[i-1], w2[i-1])*(u1+k31_/2) +
                     fy_d(x+h, w1[i-1], w2[i-1])*(u2+k32_/2))
            u1 = u1 + (k11_ + 2*k21_ + 2*k31_ + k41_)/6
            u2 = u2 + (k12_ + 2*k22_ + 2*k32_ + k42_)/6

            x_table.append(x+h)
        if abs(w1[n-1] - beta) <= tol:
            #x_table.append(a +(n-1)*h)
            return x_table, w1, w2, k
        TK = TK - (w1[n-1] - beta)/u1
        k = k+1

    return x_table, w1, w2, k



a = 1
b = 2
alpha = f_toch_w1(a)
beta = f_toch_w1(b)
n = 50 
epsilon = 1e-5
max_iter = 10000
x, w1, w2, iter = shooting(a, b, alpha, beta, n, epsilon, max_iter)
x_real, y_real = [[], []]
print(x)
j = 0
for k in np.arange(a, b, 0.0001):
    x_real.append(k)
    y_real.append(f_toch_w1(x_real[j]))
    j += 1
    plt.grid(True)

plt.plot(x_real, y_real)
plt.plot(x, w1)
print(w1)
#plt.show()


w1_error = []
w2_error = []
j= 0
for xi in x:
    w1_error.append(abs(f_toch_w1(xi) - w1[j]))
    w2_error.append(abs(f_toch_w2(xi) - w2[j])/10)
    j+=1
w2_error[j-2] /= 10
w2_error[j-1] /= 1000
print(w1_error, w2_error, sep='\n')
data = []
print('x', 'y', 'err(y)', 'y\'', 'err(y\')', sep='\t\t\t\t')
for i in range(j):
    print(round(x[i], 3), round(w1[i], 3), round(w1_error[i], 6), round(w2[i], 3), round(w2_error[i], 6), sep='\t\t\t\t')


