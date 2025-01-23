from task1 import *
def f1(x,u1,u2):
    return u1+3*u2

def f2(x,u1,u2):
    return -u1+5*u2

def u1_corr(x):
    return 3*exp(2*x)

def u2_corr(x):
    return exp(2*x)



def rk43(x,u1,u2,n,h):
    for i in range(1, n + 1):
        u1.append(u1[i-1] + deltaY43(x[i - 1], u1[i - 1], u2[i - 1], h, f1))
        u2.append(u2[i-1] + deltaY43(x[i - 1], u1[i - 1], u2[i - 1], h, f2))

def deltaY43(x, u1, u2, h, numberU):

    k11 = h*f1(x, u1, u2)
    k12 = h * f2(x, u1, u2)
    k21 = h * f1(x + (1/3) * h, u1 + (1/3) * k11, u2 + (1/3) * k12)
    k22 = h * f2(x + (1/3) * h, u1 + (1/3) * k11, u2 + (1/3) * k12)
    k31 = h * f1(x + 2/3 * h, u1 - 1/3 * k11 + k21, u2 - 1/3 * k12 + k22)
    k32 = h * f2(x + 2/3 * h, u1 - 1/3 * k11 + k21, u2 - 1/3 * k12 + k22)
    k41 = h * f1(x + h, u1 + k11 - k21 + k31, u2 + k12 - k22 + k32)
    k42 = h * f2(x + h, u1 + k11 - k21 + k31, u2 + k12 - k22 + k32)

    if (numberU):
        return 1/8 * (k11 + 3*k21 + 3*k31 + k41)
    else:
        return 1/8 * (k12 + 3*k22 + 3*k32 + k42)

def errorS2(u1n,u12n,u2n,u22n,p):
    return max(abs(u1n - u12n) / (pow(2, p) - 1),abs(u2n - u22n) / (pow(2, p) - 1));

def step2(n,a,b,u10,u20,p,sizeH,e0):
    x=[]
    u1n=[]
    u2n=[]
    u1n.append(u10)
    u2n.append(u20)
    uniform_partition(x, n, a, b)
    h = abs(x[1] - x[0])
    rk42(x, u1n,u2n, n, h)
    #plt.plot(x, u1n,x,u1n,'ro')
    x=[]
    u12n = []
    u22n = []
    u12n.append(u10)
    u22n.append(u20)
    uniform_partition(x, 2*n, a, b)
    print(x)
    h = abs(x[1] - x[0])
    rk43(x, u12n,u22n, 2*n, h)
    i = 2
    e2 = errorS2(u1n[int((i / 2) * n)], u12n[i * n], u2n[int((i / 2) * n)], u22n[i * n], p)
    e1 = e2 + 1
    count=0
    while (e2 > e0 and count<4 and h > sizeH):
        i = 2 * i
        x = []
        uniform_partition(x, i * n, a, b)
        h = abs(x[1] - x[0])
        u1n = u12n
        u2n = u22n
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
    plt.plot(x, u12n)
    plt.grid(True)
    plt.plot(x,u22n)



def task2():
    p = 4
    print('Input interval:')
    a = 0
    b = 3
    print('Input n:')
    n = 20
    print('Input y0:')
    # y0 = 2.2
    u10=3
    u20=1
    print('Input e0:')
    e0 = pow(10, -16)
    print('Input min size h:')
    sizeH = pow(10, -6)
    x = []
    u1 = []
    u2 = []
    y_toch = []
    u1.append(u10)
    u2.append(u20)
    uniform_partition(x, n, a, b)
    h = abs(x[1] - x[0])
    rk42(x,u1,u2,n,h)
    step2(n,a,b,u10,u20,p,sizeH,e0)
    x_real, y_real = [[], []]
    j = 0
    for k in np.arange(a, b, 0.0001):
        x_real.append(k)
        #y_real.append(f_corr(x_real[j]))
        j += 1
    plt.grid(True)
    plt.show()




task2()