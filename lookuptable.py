import math
lookup_table = {}

# take the hit up-front to reduce future time complexity
for n in range(1, 1001):
    lookup_table[n] = 1 / math.sqrt(n)


def inv_sqrt(n):
    # if n not in lookup_table:
    #     lookup_table[n] = 1 / math.sqrt(n)
    return lookup_table[n]


print(inv_sqrt(10))
print(inv_sqrt(100))
