from math import sin, exp, cos
import matplotlib.pyplot as plt


def f_toch(x):
    c=2*exp(1.4)
    return 0.5*x+c*exp(-x)-0.5
#0.5*x+8.1104*exp(-x)-0.5


def f(x, y):
    return cos(y)/(1.25+x)-0.1*y*y
           #1-sin(2*x+y) + 0.3*y/(x+2)
           #x/2 - y
#cos(y)/(1.25+x)-0.1*y*y

def uniformPartition(x, n, a, b):
    for i in range(n + 1):
        x.append(a + ((b - a) / n) * i)



def euler(x,y,n):
    for i in range(1,n+1):
        y.append(y[i-1]+(x[i]-x[i-1])*f(x[i-1],y[i-1]))

def rk33(x,y,n,h):
    for i in range(1, n + 1):
        y.append(y[i-1]+deltaY(x[i-1],y[i-1],h))

def deltaY(x,y,h):
    k1=h*f(x,y)
    k2=h*f(x+0.5*h,y+0.5*k1)
    k3=h*f(x+0.75*h,y+0.75*k2)
    return 1/9 * (2*k1+3*k2+4*k3)

def error(yn, y2n, p):
    return abs(yn-y2n)/(pow(2, p) - 1)

def step(n,a,b,y0,p,sizeH,e0,method):
    x=[]
    yn=[]
    yn.append(y0)
    uniformPartition(x, n, a, b)
    h = abs(x[1] - x[0])
    if(method):
        rk33(x, yn, n, h)
        plt.plot(x,yn,x,yn,'ro')
    else:
        euler(x,yn,n)
        plt.plot(x, yn, x, yn, 'ro')
    x=[]
    y2n = []
    uniformPartition(x, 2*n, a, b)
    print(x)
    h = abs(x[1] - x[0])
    y2n.append(y0)
    if (method):
        rk33(x, y2n, 2*n, h)
    else:
        euler(x, y2n, 2*n)
    i = 2
    e2 = error(yn[int((i / 2) * n)], y2n[i * n], p)
    e1 = e2 + 1
    count=0
    while (e2 > e0 and count<4 and h > sizeH):
        i = 2 * i
        x = []
        uniformPartition(x, i * n, a, b)
        h = abs(x[1] - x[0])
        yn = y2n
        y2n = []
        y2n.append(y0)
        if (method):
            rk33(x, y2n, i*n, h)
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
    plt.plot(x, y2n)
    plt.grid(True)
    plt.show()
    plt.plot(x, y2n)

def task1():
    p=3
    print('Input interval:')
    #a = 1.4
    a=0
    #b = 3.4
    b=20
    print('Input n:')
    n = 15
    print('Input y0:')
    #y0 = 2.2
    y0=0
    print('Input e0:')
    e0 = pow(10,-2)
    print('Input min size h:')
    sizeH = pow(10, -5)
    x=[]
    ye=[]
    yrg33=[]
    y_toch=[]
    ye.append(y0)
    yrg33.append(y0)
    uniformPartition(x,n,a,b)
    h=abs(x[1]-x[0])
    euler(x,ye,n)
    print(x)
    print(ye)
    rk33(x,yrg33,n,h)
    step(n,a,b,y0,p,sizeH,e0,1)
   # plt.plot(x, yrg33, x, yrg33, 'ro')
    #plt.grid(True)
   # plt.show()
  #  for i in range(n+1):
    #    y_toch.append(f_toch(x[i]))
   # plt.plot(x, y_toch, x, y_toch, 'ro')
   # plt.grid(True)
   # plt.show()
   # print("Error y_toch - yn:")
   # print(error(y_toch[n],ye[n],p))

def f1(x,u1,u2):
    return u1+3*u2

def f2(x,u1,u2):
    return -u1+5*u2

def rk42(x,u1,u2,n,h):
    for i in range(1, n + 1):
        u1.append(u1[i-1]+deltaY42(x[i-1],u1[i-1],u2[i-1],h,True))
        u2.append(u2[i-1]+deltaY42(x[i-1],u1[i-1],u2[i-1],h,False))

def deltaY42(x,u1,u2,h,numberU):
    k11 = h * f1(x, u1, u2)
    k12 = h * f2(x, u1, u2)
    k21 = h * f1(x + (1 / 3) * h, u1 + (1 / 3) * k11, u2 + (1 / 3) * k12)
    k22 = h * f2(x + (1 / 3) * h, u1 + (1 / 3) * k11, u2 + (1 / 3) * k12)
    k31 = h * f1(x + 2 / 3 * h, u1 - 1 / 3 * k11 + k21, u2 - 1 / 3 * k12 + k22)
    k32 = h * f2(x + 2 / 3 * h, u1 - 1 / 3 * k11 + k21, u2 - 1 / 3 * k12 + k22)
    k41 = h * f1(x + h, u1 + k11 - k21 + k31, u2 + k12 - k22 + k32)
    k42 = h * f2(x + h, u1 + k11 - k21 + k31, u2 + k12 - k22 + k32)

    if (numberU):
        return 1 / 8 * (k11 + 3 * k21 + 3 * k31 + k41)
    else:
        return 1 / 8 * (k12 + 3 * k22 + 3 * k32 + k42)

def errorS2(u1n,u12n,u2n,u22n,p):
    return max(abs(u1n - u12n) / (pow(2, p) - 1),abs(u2n - u22n) / (pow(2, p) - 1));

def step2(n,a,b,u10,u20,p,sizeH,e0):
    x=[]
    u1n=[]
    u2n=[]
    u1n.append(u10)
    u2n.append(u20)
    uniformPartition(x, n, a, b)
    h = abs(x[1] - x[0])
    rk42(x, u1n,u2n, n, h)
    plt.plot(x, u1n,x,u1n,'ro', label='u1')
    x=[]
    u12n = []
    u22n = []
    u12n.append(u10)
    u22n.append(u20)
    uniformPartition(x, 2*n, a, b)
    print(x)
    h = abs(x[1] - x[0])
    rk42(x, u12n,u22n, 2*n, h)
    i = 2
    e2 = errorS2(u1n[int((i / 2) * n)], u12n[i * n], u2n[int((i / 2) * n)], u22n[i * n], p)
    e1 = e2 + 1
    count=0
    while (e2 > e0 and count<4 and h > sizeH):
        i = 2 * i
        x = []
        uniformPartition(x, i * n, a, b)
        h = abs(x[1] - x[0])
        u1n = u12n
        u2n=u22n
        u12n = []
        u22n=[]
        u12n.append(u10)
        u22n.append(u20)
        rk42(x, u12n,u22n, i*n, h)
        if (e2 >= e1):
            count += 1
        else:
            e1 = e2
            count=0
        e2 = errorS2(u1n[int((i / 2) * n)], u12n[i * n], u2n[int((i / 2) * n)], u22n[i * n], p)
    if (e2 <= e0):
        print("Error=0 – завершение в соответствии с назначенным условием о достижении заданной точности:")
        print(errorS2(u1n[int((i / 2) * n)], u12n[i * n], u2n[int((i / 2) * n)], u22n[i * n], p))
        print("Number of partition intervals:")
        print(i * n)
    if (count>=3):
        print("Error=1 – процесс решения прекращен, т.к. с уменьшением шага погрешность не уменьшается:")
        print("Error:")
        print(errorS2(u1n[int((i / 2) * n)], u12n[i * n], u2n[int((i / 2) * n)], u22n[i * n], p))
        print("Number of partition intervals:")
        print(i * n)
    if (h <= sizeH):
        print("Error=2 - процесс решения прекращен, т.к. значение шага стало недопустимо малым:")
        print(errorS2(u1n[int((i / 2) * n)], u12n[i * n], u2n[int((i / 2) * n)], u22n[i * n], p))
        print("Number of partition intervals:")
        print(i * n)
    plt.plot(x, u12n, label='u1')
    plt.grid(True)
    plt.legend()
    plt.show()
    plt.plot(x,u22n, label = 'u2 computed')



def task2():
    p = 4
    print('Input interval:')
    a = 0
    b = 3
    print('Input n:')
    n = 15
    print('Input y0:')
    # y0 = 2.2
    u10=3
    u20=1
    print('Input e0:')
    e0 = pow(10, -16)
    print('Input min size h:')
    sizeH = pow(10, -5)
    x = []
    u1 = []
    u2 = []
    y_toch = []
    u1.append(u10)
    u2.append(u20)
    uniformPartition(x, n, a, b)
    h = abs(x[1] - x[0])
    rk42(x,u1,u2,n,h)
    step2(n,a,b,u10,u20,p,sizeH,e0)
    #for i in range(n+1):
        #y_toch.append(f_toch(x[i]))
    plt.plot(x, u2, x, u2,'ro', label='u2')
    plt.grid(True)
    plt.legend()
    plt.show()




task2()