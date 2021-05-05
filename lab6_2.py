def genf(n):
    for d in range(1,n):
        if n % d == 0:
            yield d

line = genf(100)
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))
print(next(line))


