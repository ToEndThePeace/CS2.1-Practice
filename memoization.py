"""
0 1 1 2 3 5 8 13 21 34 55 89 144...

How do you find the nth fibonacci number?
"""

cache = {}


def fib(n):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


for i in range(10000):
    print(f"{i:3}: {fib(i)}")
