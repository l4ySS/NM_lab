from math import sin, exp, cos
import matplotlib.pyplot as plt
import numpy as np

# 27
# y' = x**2 + y/3
# a = 0.3
# y(a) = 0.9
def f_corr(x):
    c = 6057 / (100 * exp(1/10))
    return c*exp(x/3) - 3*x**2 - 18*x - 54


def f(x, y):
    return x**2 + y/3
           #1-sin(2*x+y) + 0.3*y/(x+2)
           #x**2 + y/3
           #cos(1.5*x+y) - 2.25*(x-y)


def uniform_partition(x, n, a, b):
    for i in range(n + 1):
        x.append(a + ((b - a) / n) * i)


def euler(x, y, n):
    for i in range(1, n+1):
        y.append(y[i-1]+(x[i]-x[i-1])*f(x[i-1], y[i-1]))


def rk32(x, y, n, h):
    for i in range(1, n + 1):
        y.append(y[i-1] + d_y(x[i-1], y[i-1], h))


def d_y(x, y, h):
    k1 = h*f(x, y)
    k2 = h*f(x+h/3, y+k1/3)
    k3 = h*f(x+2*h/3, y+2*k2/3)
    return 1/4 * (k1+3*k3)


def error(yn, y2n, p):
    return abs(yn-y2n)/(pow(2, p) - 1)



def step(n,a,b,y0,p,sizeH,e0,method):
    x=[]
    yn=[]
    y_table = []
    yn.append(y0)
    uniform_partition(x, n, a, b)
    h = abs(x[1] - x[0])



    x_real, y_real = [[], []]
    j = 0
    for k in np.arange(a, b, 0.0001):
        x_real.append(k)
        y_real.append(f_corr(x_real[j]))
        j += 1

    plt.plot(x_real, y_real, label='f(x)')
    if(method):
        rk32(x, yn, n, h)

    else:
        euler(x,yn,n)

    x=[]
    y2n = []
    uniform_partition(x, 2*n, a, b)
    print(x)
    h = abs(x[1] - x[0])
    y2n.append(y0)
    if (method):
        rk32(x, y2n, 2*n, h)
    else:
        euler(x, y2n, 2*n)
    i = 2
    e2 = error(yn[int((i / 2) * n)], y2n[i * n], p)
    e1 = e2 + 1
    count=0
    while (e2 > e0 and count<4 and h > sizeH):
        i = 2 * i
        x = []
        uniform_partition(x, i * n, a, b)
        h = abs(x[1] - x[0])
        yn = y2n
        y2n = []
        y2n.append(y0)
        if (method):
            rk32(x, y2n, i*n, h)
        else:
            euler(x, y2n, i*n)
        if (e2 >= e1):
            count += 1
        else:
            e1 = e2
            count=0
        e2 = error(yn[int((i / 2) * n)], y2n[i * n], p)
    if (e2 <= e0):
        print("Error=0 – завершение в соответствии с назначенным условием о достижении заданной точности:")
        print(error(yn[int((i / 2) * n)], y2n[i * n], p))
        print("Number of partition intervals:")
        print(i * n)
    if (count>=3):
        print("Error=1 – процесс решения прекращен, т.к. с уменьшением шага погрешность не уменьшается:")
        print("Error:")
        print(error(yn[int((i / 2) * n)], y2n[i * n], p))
        print("Number of partition intervals:")
        print(i * n)
    if (h <= sizeH):
        print("Error=2 - процесс решения прекращен, т.к. значение шага стало недопустимо малым:")
        print(error(yn[int((i / 2) * n)], y2n[i * n], p))
        print("Number of partition intervals:")
        print(i * n)
    plt.plot(x, y2n, label='result')



    plt.grid(True)
    plt.legend()



def task1():
    p=3
    print('Input interval:')
    a = 0.3
    b = 2.3
    print('Input n:')
    n = 20
    print('Input y0:')
    y0 = 0.9

    print('Input e0:')
    e0 = pow(10,-8)
    print('Input min size h:')
    sizeH = pow(10, -5)
    x=[]
    ye=[]
    yrg32=[]
    y_toch=[]
    ye.append(y0)
    yrg32.append(y0)
    uniform_partition(x,n,a,b)
    h=abs(x[1]-x[0])
    euler(x,ye,n)
    print(x)
    print(ye)
    rk32(x,yrg32,n,h)
    plt.figure('Euler')
    step(n,a,b,y0,p,sizeH,e0,0)
    plt.figure('Runge-Kutta')

    step(n, a, b, y0, p, sizeH, e0, 1)
    #plt.plot(x, yrg32, x, yrg32, 'ro')
    #plt.grid(True)
    plt.show()
    #for i in range(n+1):
     #   y_toch.append(y_toch(x[i]))
    #plt.plot(x, y_toch, x, y_toch, 'ro')
    #plt.grid(True)
    #plt.show()
    #print("Error y_toch - yn:")
    #print(error(y_toch[n],ye[n],p))

task1()