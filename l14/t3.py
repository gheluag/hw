def fib():
    a= 0
    b = 1
    for m in range(10):
        yield a
        a, b = b, a + b

print(list(fib()))