"""
0 1 1 2 3 5 8 13 21 34 55 89 144...

How do you find the nth fibonacci number?
"""


def fib(n):
    cache = {}

    def fibr(n):
        if n <= 1:
            return n
        if n not in cache:
            cache[n] = fibr(n - 1) + fibr(n - 2)
        return cache[n]
    return fibr(n)


for i in range(200):
    print(f"{i:3}: {fib(i)}")
