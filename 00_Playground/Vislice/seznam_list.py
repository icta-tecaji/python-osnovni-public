# LIST

#    0  1  2  3  4    5      6            7
#   -8 -7 -6 -5 -4   -3     -2           -1
x = [1, 2, 5, 4, 5, None, "asndi", [12345, [969]]]
print()
# print(x[0], x[-8])
# print(x[4], x[-4])
# print(x[7][1][0], x[-1][-1][-1])
# print(len(x))


# <spremenljivka>[<start_index>:<stop_index>:<step_size>]
# print(x)
# print(x[3:])
# print(x[3:][::-1])

# print(x.index("asndi"))

# print("anze".replace("a", "A"))

x2 = [(10 if el == 4 else el) for el in x]

x3 = []
for el in x:
    if el == 4:
        x3.append(10)
    else:
        x3.append(el)

# print(x)
# print(x2)
# print(x3)


x4 = x.copy()
x4.remove(5)
x5 = [el for el in x if el != 5]

# print(x)
# print(x4)
# print(x5)
# print(type(x))

a = 1
b = 2
a, b = b, a

split_index = 5
a, b = x[:split_index], x[split_index:]

# print(x)
# print(a)
# print(b)


# print()
# print(x[2:7])

# print()
# print(x[-4:-1])

# print(x)
# x[0] = [[123, 123]]
# print(x)
# del x[0]
# print(x)

# print(x)
# x.append(3)
# print(x)

# temp = x.pop()
# print(temp)
# print(x)

a = (1, 3, 4, 56)
print(type(a), a)
a = list(a)
print(type(a), a)


# Naloga:

# Pri sledečem list-u začnite z vrednostjo 4 in vzemite vsako 3 vrednost.

# ```python
# our_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Rešitev:
# [4, 7, 10, 13, 16, 19]
# ```
our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
resitev = our_list[3::3]
print(resitev)


# fibonacci
# x = int(input("Dolžina Fibonnacicijevega zaporedja: "))
# counter = 2
# fibonacci = [0, 1]
# while counter < x:
#     fibonacci.append(fibonacci[-1] + fibonacci[-2])
#     counter += 1
# print(fibonacci)

x = []
x = list()

a = [1, 2, 3]
b = [6, 7, 8]
x = a + b

print(x)

a.extend(b)
print(a)
print(b)


print("=" * 100)


# x =  [ <element-i>*10 for <element-i> in <iterable> if <expression> ]
# x =  { <element-i>*10 for <element-i> in <iterable> if <expression> }

# # x = []
# x = set()
# for <element-i> in <iterable>:
#     if <expression>:
#         # x.append(<element-i>*10)
#         x.add(<element-i>*10)


# def fun(a):
#     return a * 12


# x = fun

# x = lambda a: a * 12
# x1 = lambda a: a * 4
# x2 = lambda a: a * 8
# print(x(8))
# print(x1(8))
# print(x2(8))
