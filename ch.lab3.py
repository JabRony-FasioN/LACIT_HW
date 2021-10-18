import math

A = [[11.4, 6.1, -1.7], 
     [3.9, 12.8, -1.2], 
     [3.7, 2.1, -10.7]]

B = [-7.2,-8.0, 13.2]

A_try = A.copy()
B_try = B.copy()

def Fin(a,b):
    print(abs(a) - abs(b))    

def Show(a, b):
    for row in range(len(B)):
        print("( ", end = "")
        for col in range(len(A[row])):
            print(a[row][col], " ",end = "")
        print(" |",b[row], ")")
    print("\n")

def Swap(a, b, r1, r2):
    a[r1], a[r2] = a[r2], a[r1]
    b[r1], b[r2] = b[r2], b[r1]

def Divide(a, b, r, div):
    a[r] = [a / div for a in a[r]]
    b[r] /= div

def Combine(a, b, r, temp_r, aim):
    a[r] = [(a + k * aim) for a, k in zip(a[r], a[temp_r])]
    b[r] += b[temp_r] * aim

def form(a,b):
    for i in range(len(a)):
        a[i].append(b[i])
    
def Gauss(a,b):
    col = 0 
    while (col < len(b)):
        current_r = None
        for r in range(col, len(a)):
            if current_r is None or abs(a[r][col]) > abs(a[current_r][col]):
                current_r = r
        if current_r is None:
            print("нет решений")
            return None
        Show(a,b)

        if current_r != col:
            Swap(a, b, current_r, col)
            Show(a,b)
        Divide(a, b, col, a[col][col])
        Show(a,b)
        for r in range(col + 1, len(a)):
            Combine(a, b, r, col, -a[r][col])
        Show(a, b)
        col += 1
    X = [0 for x in b]
    for i in range(len(b) -1, -1, -1):
        X[i] = b[i] - sum(j * a for j, a in zip(X[(i + 1) :], a [i][(i + 1):]))
    print("\n".join("X{0} =\t{1}".format(i + 1, j) for i,j in enumerate(X)))
    sum_help = []
    for row in range(len(B_try)):
        print("( ", end = "")
        for col in range(len(A_try[row])):
            print(A_try[row][col] * X[col], " ",end = "")
            sum_help.append(A_try[row][col] * X[col])
        print(" |",B_try[row] , ")")
    print("\n")
    list1 = sum_help[0:3]
    list2 = sum_help[3:6]
    list3 = sum_help[6:9]
    
    Fin(B_try[0], sum(list1))
    Fin(B_try[1], sum(list2))
    Fin(B_try[2], sum(list3))
    return X

def transform(matrix):
    m = matrix
    for i in range(n):
        r = matrix[i][i]
        for j in range(n+1):
            m[i][j] = matrix[i][j]/r
    for i in range(n):
        m[i][i] = 0
        for j in range(n):
            m[i][j] = - m[i][j]
    return(m)

def zeidel(matrix, vector):
    z = [vector[i] for i in range(n)]
    for i in range(n):
        s = 0
        for j in range(n):
            s += matrix[i][j]*z[j]
        z[i] = s + matrix[i][n]
    return(z)
    
def norm(vector1, vector2):
    d = [0 for i in range(n)]
    for i in range(n):
        d[i] = math.fabs(vector1[i] - vector2[i])
    return max(d)
def round_eps(vector, e):
    k = 0
    while e < 1:
        e *=10
        k +=1
    d = [0 for i in range(n)]
    for i in range(n):
        d[i] = round(vector[i],k)
    return d

while True:
    goal = int(input("Введите номер метода: \n 1 - Гаусса \n 2 - итерации \n 0 - Выход с программы "))
    if goal == 1:
        Gauss(A,B)
    if goal == 2: 
        form(A,B)
        n =3
        eps = 0.0000001
        alfa = transform(A)
        x1 = [0 for i in range(n)]
        x2 = zeidel(alfa,x1)
        k = 0
        while norm(x1,x2) > eps:
            x1 = x2
            x2 = zeidel(alfa,x1)
            k+=1 
        print('Решение системы с точностью', eps)
        print(x2) 
        print('Количество итераций',k)
    if goal == 0:
        raise SystemExit


# 2) гаусса подстановка = сумма уравнения - свободный член уравнения (разница или погрешность)