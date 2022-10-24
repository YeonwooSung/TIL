def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))

for i in range(10):
    print(next(fib))

print(next(fib))
print(next(fib))
