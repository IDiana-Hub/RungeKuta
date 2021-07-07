import matplotlib.pyplot as plt #бібліотека для створення графіків
from math import *
def f(x,y):
    return eval(func)
def p2(x,y,h,A): #метод 2-го порядку
    global X2, Y2
    i=0; n=abs((A-x0)/h)
    while i<n:
        k1=f(x,y); i+=1
        k2=f(x+h/2,y+h/2*k1)
        dy=h*k2
        y+=dy; x+=h
        if x0<A:
            X2.insert(0, x); Y2.insert(0, y)
        else:
            X2.append(x); Y2.append(y);
def p3(x,y,h,A):  #метод 3-го порядку
    global X3, Y3
    i=0; n=abs((A-x0)/h)
    while i<n:
        k1=f(x,y); i+=1
        k2=f(x+h/2,y+h/2*k1)
        k3=f(x+h, y-h*k1+2*h*k2)
        dy=h/6*(k1+4*k2+k3)
        y+=dy; x+=h
        if x0<A:
            X3.insert(0, x); Y3.insert(0, y)
        else:
            X3.append(x); Y3.append(y);
def p4(x,y,h,A): #метод 4-го порядку
    global X4, Y4
    i=0; n=abs((A-x0)/h)
    while i<n:
        k1=f(x,y); i+=1;
        k2=f(x+h/2, y+h*k1/2)
        k3=f(x+h/2, y+h*k2/2)
        k4=f(x+h, y+h*k3)
        dy=h/6*(k1+2*k2+2*k3+k4)
        y+=dy; x+=h
        if x0<A:
            X4.insert(0, x); Y4.insert(0, y)
        else:
            X4.append(x); Y4.append(y);
def pn4(x,y,h,A): #неявний метод 4-го порядку
    global XN4, YN4
    i=0; n=abs((A-x0)/h)
    while i<n:
        K=[-100, 0]; j=1;
        while K[j]-K[j-1]>(h/100):
            K.append(f(x+h/2,y+h/2*K[j])); j+=1;
        k1=max(K); j=1; K.clear(); K=[-100, 0]
        while K[j]-K[j-1]>(h/100):
            K.append(f(x+2*h/3, y+h*2/3*K[j])); j+=1;
        k2=max(K); j=1; K.clear(); K=[-100, 0]
        while K[j]-K[j-1]>(h/100):
            K.append(f(x+h/2, y+h*(-5*k1/2+5*k2/2+K[j]/2))); j+=1;
        k3=max(K); j=1; K.clear(); K=[-100, 0]
        while K[j]-K[j-1]>(h/100):
            K.append(f(x+h/3, y+h*(-5*k1/3+4*k2/3+2*K[j]/3))); j+=1;
        k4=max(K)
        dy= h *(-k1+3*k2/2-k3+3*k4/2)
        y+=dy; x+=h; i+=1
        if x0<A:
            XN4.insert(0, x); YN4.insert(0, y)
        else:
            XN4.append(x); YN4.append(y);
func=input("Введіть функцію у'(х,у)= \n")
x0=float(input("х0="))
y0=float(input("y0="))
a=float(input("Знайти на відрізку від "))
b=float(input("до "))
H=float(input("із кроком  "))
X2=list(); Y2=list()
X3=list(); Y3=list()
X4=list(); Y4=list()
XN4=list(); YN4=list()
if x0>a:
    p2(x0,y0,-H,a)
    p3(x0,y0,-H,a)
    p4(x0,y0,-H,a)
    pn4(x0,y0,-H,a)
p2(x0,y0,H,b)
p3(x0,y0,H,b)
p4(x0,y0,H,b)
pn4(x0,y0,H,b)
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()
plt.plot(X2,Y2, label = "2p")
plt.plot(X3,Y3,label = "3p")
plt.plot(X4,Y4,label = "4p")
plt.plot(XN4,YN4,label = "4np")
plt.legend()
print(Y2,"\n", Y3, "\n", Y4, "\n", YN4 )
plt.show()
print("finish")
