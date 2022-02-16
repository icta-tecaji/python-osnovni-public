# List

živali = ["pingvin", "medved", "los", "volk"]
print(type(živali))
print(živali)


# Lists are odered
a = ["pingvin", "medved", "les", "volk"]
b = ["los", "medved", "pingvin", "volk"]
print(a == b)

# List can contain arbitrary object
a = [122.12, "medved", 3, False, 2+3j, "medved"]
print(type(a))
print(a)

# List elements can be accessed by index
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(a[0])
print(a[-1])
print(a[-6])

## Slicing
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
slice = a[1:4]
print(slice)

slice = a[-5:-2]
print(type(slice))
print(slice)

slice = a[:4]
print(slice)

slice = a[2:]
print(slice)

slice = a[::2]
print(slice)

print(a[2:5:2])
print(a[::-1])

# Lists can be nested to arbitrary depth
x = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hh", "ii"], "j"]

a = ["bb", ["ccc", "ddd"], "ee", "ff"] #x[1]
b = ["ccc", "ddd"] #a[1]
c = "ccc"#b[0]
print(type(c))
print(c)

print(x[1][1][0])


# lists are mutable
a = ["pingvin", "medved", "los", "volk"]
print(a)

a[2] = "koza"
print(a)



a = ["pingvin", "medved", "los", "volk"]
print(a)
del a[3]
print(a)
print()


a = ["pingvin", "medved", "los", "volk"]
print(a)
a.append([1,2,3,4])
print(a)
print()

a = ["pingvin", "medved", "los", "volk"]
print(a)
a.extend([1,2,3,4])
print(a)
print()

a = ["pingvin", "medved", "los", "volk"]
print(a)
a.insert(1, 100)
print(a)
print()

a = ["pingvin", "medved", "los", "volk"]
print(a)
a.remove("los")
print(a)
print()


a = ["pingvin", "medved", "los", "volk"]
print(a)
b = a.pop(1)
print(b)
print(a)
print()



# lists are dynamic
a = [1,2,3,4,5]
print(type(a))
print(a)

a = 123
print(type(a))
print(a)


'''
Naloga: Iz sledečega list-a pridobite vrednost **ffff**
our_list = ["a", ["bb", "cc"], "d", [["eee"], ["ffff"], "ggg"]]
'''
# Rešitev
our_list = ["a", ["bb", "cc"], "d", ]
a = our_list[-1]
b = a[1]
c = our_list[-1][1][0]

print(c)
print(type(c))


''''
Naloga: Ustvarite nov list tako, da pri sledečem list-u začnite z 
vrednostjo 4 in vzemite vsako 3 vrednost.
our_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
'''
# Rešitev


