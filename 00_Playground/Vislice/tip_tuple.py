# TUPLE

# x = (1, 2, 3, 4, 5)
# print(x, type(x), id(x))
# x = tuple(7 if el == 1 else el for el in x)
# print(x, type(x), id(x))

# x = list(x)
# print(x, type(x), id(x))
# x[0] = 7
# print(x, type(x), id(x))
# print()


x = (1, 2, 4, 5, 6, [1, 2, 3])
# print(type(x), x, id(x))
# x[-1][0] = 7
# print(type(x), x, id(x))

print(x[-4:])

x = (1,)
print(type(x), x)

x = tuple()
print(type(x), x)
