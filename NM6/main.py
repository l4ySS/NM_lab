from math import exp
#u=x^3
#u'=3*x^2=w
#u''=6*x=f(x,u,w)

def f_toch_u(x):
    return x*x*x
def f_toch_w(x):
    return 3*x*x
def f(x, u, w):
    return 12*u/w + 2*x

def wFunc(x,u):
    return 3*u/x


def rk4242(x,u,w,n,h):
    for i in range(1, n + 1):
        w.append(w[i-1]+deltaY4242(x[i-1],u[i-1],w[i-1],h,True))
        u.append(u[i-1]+deltaY4242(x[i-1],u[i-1],w[i-1],h,False))

def deltaY4242(x,u,w,h,numberU):
    w_k1=h*f(x,u,w)
    u_k1 = h * wFunc(x, u)
    w_k2=h*f(x+0.25*h,u+0.25*u_k1,w+0.25*w_k1)
    u_k2 = h * wFunc(x + 0.25 * h, u + 0.25 * u_k1)
    w_k3=h*f(x+0.5*h,u+0.5*u_k2,w+0.5*w_k2)
    u_k3 = h * wFunc(x + 0.5 * h, u + 0.5 * u_k2)
    w_k4=h*f(x+h,u+u_k1-2*u_k2+2*u_k3,w+w_k1-2*w_k2+2*w_k3)
    u_k4 = h * wFunc(x + h, u + u_k1 - 2 * u_k2 + 2 * u_k3)
    if (numberU):
        return (w_k1+4*w_k3+w_k4)*1/6
    else:
        return (u_k1 + 4 * u_k3 + u_k4)*1/6


def uniformPartition(x, n, a, b):
    for i in range(n + 1):
        x.append(a + round((b - a) / n * i,2))


def step1():
    a=1
    b=2
    A=1
    B=8
    B1=12
    e=0.00001
    n=10
    alpha0=9
    alpha1=1
    L=0
    x=[]
    uniformPartition(x,n,a,b)
    u=[]
    u.append(A)
    w=[]
    w.append(alpha0)
    h=0.1
    print(h)
    print("x=", x)
    rk4242(x,u,w,n,h)
    print("u=",u)
    print("w=", w)
    alpha=alpha0
    if(abs(w[n]-B)>=e):
        wn=w[n]
        u=[]
        w=[]
        u.append(A)
        w.append(alpha1)
        rk4242(x, u, w, n, h)
        L=1
        alpha=alpha1


    while(abs(w[n]-B1)>=e):
        alpha = alpha1 - ((w[n] - B1) * (alpha1 - alpha0)) / ((w[n]-B1) - (wn-B1))
        wn = w[n]
        u = []
        w = []
        u.append(A)
        w.append(alpha)
        alpha0 = alpha1
        alpha1 = alpha
        rk4242(x, u, w, n, h)
        L = L + 1

    print("x=", x)
    print("u=", u)
    print("w=", w)
    print("alpha=", alpha)
    print("L =", L)
    ftu=[]
    ftw=[]
    for i in range(n+1):
        ftu.append(f_toch_u(x[i]))
        ftw.append(f_toch_w(x[i]))
    print("u_toch=", ftu)
    print("w_toch=", ftw)
    ftue = []
    ftwe = []
    for i in range(n + 1):
        ftue.append(abs(ftu[i]-u[i]))
        ftwe.append(abs(ftw[i]-w[i]))
    print("u_toch_e=", ftue)
    print("w_toch_e=", ftwe)
step1()
