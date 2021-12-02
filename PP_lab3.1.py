import numpy as np
import random
#11
"""
n = int(input("количество элементов в массиве: "))
k = int(input("Кратное число итерации: "))
N = [random.randint(0, 30) for i in range(n)]
A = np.array(N)
print(A)

aim = slice(0,n,k)
goal = A[aim]
goal = np.delete(goal,0)
print(goal)
"""
"""
#39 ИСПРАВИТЬ
n = int(input("количество элементов в массиве: "))
N = [random.randint(0, 30) for i in range(n)]
A = np.array(N)
print(A)
i = 2 ; aim = 1
for i in range(n-1):
    if A[i] < A[i-1] and A[i] < A[i+1] or A[i] > A[i-1] and A[i]> A[i+1]:
        aim+=1
print(aim)
"""


#60
"""
n = int(input("количество элементов: "))
a = [random.randint(0, 30) for i in range(n)]
b = [random.randint(0, 30) for i in range(n)]
K = int(input("индекс K: "))
b[K-1] = sum(a[K-1:: ])                                              
a = np.array(a)
b = np.array(b)
print(a)
print(b)
"""
#107
"""
n = int(input("размер массива: "))
ls = [random.randint(0,30) for i in range(n)]
print(ls)
for i in range(1, len(ls), 2):
    ls[i] *= 3
print(ls)
"""
#37
"""
m = 5
n = 5
arr = np.random.randint(1,10,(m,n))
print(arr)
b = np.unique(arr[:,-1])
print(b)
c = sum(len(np.setdiff1d(b, arr[:,i])) == 0 for i in range(n-1))
print(c)
"""
#65
"""
m =3
n =4
y = []
arr = np.random.randint(-5,10,(m,n))
print(arr)
if min(arr[:,0]) > 0:
    arr = arr[:,1:] 
else:
    pass
print(arr)
"""
#96

"""
M = int(input("Размер матрицы: "))
A = np.random.randint(0,10,(M,M))
print(A)
for i in range(1,M):
    for j in range(0,i):
        A[i,j], A[j,i] = A[j,i], A[i,j]

print(A)
"""