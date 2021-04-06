L = [1,5,2,6]
L.sort()

for i in range(len(L)-1):
    for x in range(i + 1, len(L)):
        print([L[i], L[x]])