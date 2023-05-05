# LIST - ARRAY
živali = ["pingvin", "medved", "los", "volk"]
# print(type(živali), živali)

# Lists are orderd
a = ["pingvin", "medved", "los", "volk"]
b = ["los", "medved", "pingvin", "volk"]
# print(a == b)

# Lists can contain arbitrary object
a = [221.323, 12, "medved", False]
# print(type(a), a)
a = [1, 2, 2, 2, 2, 2, 2, 3, 4]
# print(type(a), a)

# List elements can be accessed by index
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
# print(a[0])
# print(a[5])
# print(a[2])
# print(a[-1])
# print(a[-2])

## Slicing
# print(a[2:5])
# print(a[-5:-2])
# print(a[:4])
# print(a[2:])
# print(a[::2])
# print(a[::-2])
# print(a[::-1])
# SLICING - a[ start : end : step]

# Lists can be nested to arbitrary depth
# a = ["a", ["bb", "cc"]]
# print(a[1])

x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# print(x[2])
y = x[1]
# print(y[2]) # print(x[1][2])

# print(x[1][1][0])

#Lists are mutable
a = ["pingvin", "medved", "los", "volk"]
# print(a)
# a[2] = "koza"
# print(a)
# del a[3]
# print(a)
# a.append(2)
# print(a)
# a.extend([1,2,3])
# print(a)
# a.insert(1, "papiga")
# print(a)
# a.remove("los")
# print(a)
# x = a.pop(2)
# print(a)
# print("Popped value", x)

# Naloga:
# Iz sledečega list-a pridobite vrednost ffff
# our_list = ["a", ["bb", "cc"], "d", [["eee"], ["ffff"], "ggg"]]
# print(our_list[3][1][0])

# Strings are Lists
# beseda = "lokomotiva"
# print(beseda[::2])