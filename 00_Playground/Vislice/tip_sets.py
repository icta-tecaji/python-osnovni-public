# SET

x = set()

x = {1, 2, 3, 4, 5}
print(type(x), x)

x.add(7)
x.add(7)
print(type(x), x)

x.update([1, 2, 3, 4, 8, 9, 0])
print(type(x), x)


x1 = {1, 2, 3, 4}
x2 = {4, 5, 6, 7}

print(x1 | x2)
print(x1.union(x2))

x = [1, 1, 1, 2, 4, 5, 6, 1, 1, 1, 1]
print(x)
x = list(set(x))
print(x)

print(set([1, 2, 3, 4]))
print(tuple({1, 2, 3}))

x = {1, 2222, 3, 4, 5, 6, 12, 3234}
print(sorted(x, key=lambda x: x))
print()


x1 = {1, 2, 3, 4}
x2 = {4, 5, 6, 7}
x3 = {66, 777, 88}

print(x1 | x2 | x3)
print(x1.union(x2).union(x3))

print(x1.intersection(x2))

print(x1.difference(x2))
print(x1 - x2)

print(x1.symmetric_difference(x2))
print(x1 ^ x2)

print(x1)
if 9 in x1:
    x1.remove(9)
else:
    x1.remove(3)

try:
    x1.remove(9)
except KeyError as err:
    print(f"Prišlo je do napake: {err}")


x1.discard(9)

print(x1)
temp = x1.pop()
print(x1)
print(temp)


# FROZEN SET
x = frozenset([1, 2, 3, 4])

print(x | {7, 8, 9})
