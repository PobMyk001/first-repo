def genFib(n):
    a, b = 0, 1
    for i in range(n + 1):
        yield a
        print(list(genFib(5)))
