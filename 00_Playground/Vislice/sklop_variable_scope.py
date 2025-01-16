# Variable scope ali "kje so vidne katere spremenljivke"


# for i in range(10):
#     print(i)

# print(i)


def fun():
    # LOKALNE SPREMENLJIVKE
    global a
    # a = 222
    # global a
    # a = a * 2
    a[2] = 77
    print(a)


# GLOBALNE SPREMENLJIVKE
a = [1, 2, 3, 4]


print(a)

fun()

print(a)
