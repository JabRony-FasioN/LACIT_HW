#x=22,26,33
import numpy as np
import matplotlib.pyplot as plt

from CM_lab4 import A
PI = 3.14
"""
def lagrange(x,y,t):
    l = 0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i!=j:
                p1 = p1*(t-x[i])
                p2 = p2*(x[j]-x[i])
        l = l + y[j]*p1/p2
    return l

x = np.array([17.00,23.00,25.00,28.00,31.00,36.00], dtype=float)
y = np.array([-8.30,-7.70,-6.90,-5.50,-4.00,-1.5], dtype=float)
xnew = np.linspace(np.min(x),np.max(x),50)
ynew = [lagrange(x,y,i) for i in xnew]
print(lagrange(x,y,100))
plt.plot(x, y,'o',xnew, ynew, lw = 2, color="black")
plt.grid(True)
plt.show()
"""
#y = sin𝜋x+3
def fun(x):
    y = 0
    y = np.sin(PI*x) + 3
    return y

def coef(x,y):
    m  = len(x)
    x= np.copy(x)
    a= np.copy(y)
    for i in range(1,m):
        a[i:m] = (a[i:m] - a[i - 1])/(x[i:m] - x[i - 1])
    return a

def newton_polynomial(x_data, y_data, x):
   
    a = coef(x_data, y_data)
    n = len(x_data) - 1  
    p = a[n]
    print(p)
    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p


a = 0
b = 2
x1 =0.03; x2 = 1.57 
n = 10
H = b/n
block_x = []; block_y = []
for i in range(n):
    block_x.append(round(H,2))
    H+=0.2

for i in range(len(block_x)):
    block_y.append(round(fun(i), 3))

print(block_y)
print(round(newton_polynomial(block_x,block_y,0.03),3))
#print(round(newton_polynomial(block_x,block_y,1.9),3))
#print(fun(0.03))
#print(fun(1.9))


