def fibo(n):
    a = 0
    b = 1

    for d in range(n):
        c = a+b
        a = b
        b = c

    return b

for a in range(10):
    print(fibo(a))
