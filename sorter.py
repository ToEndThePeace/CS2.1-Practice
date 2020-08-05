d = {
    "foo": 2,
    "bar": 12,
    "qux": 17
}
# How can i put this in alphabetical order by key?
# for key, val in d.items():
#     print(key, val)

# l = [t for t in d.items()]
l = list(d.items())
print(l)

# sort by ascending key
l.sort()
print(l)

# descending key
l.sort(reverse=True)
print(l)

# sort by ascending value
# def fun1(e):
#     _, val = e
#     return val
# l.sort(key=fun1)
# print(l)
# BUT WHY USE THIS when you can use a lambda func?
# -----\/
l.sort(key=lambda e: e[1])
print(l)
