# Tuple --> immutable

a = [1,2,3]
a[0] = 5
print(a)
print(type(a))
print()

a = (1,2,3)
#a[0] = 5
print(a)
print(type(a))
print()

a = (1,2,"niz",(1,2,3))
print(a)
print(a[0])
print(a[0::2])
print()

b = (1,2)
c = (1)
d = ()
print(type(b))
print(type(c))
print(type(d))
print()

a = (1,)
print(type(a))
print()

# list()
# tuple()
# set()
# dict()

a = [1,2,"g"]
print(type(a))
b = tuple(a)
print(b)
print(type(b))
print()

# Naloga
# Izpišite vrednost "cc"
our_tuple = ("a", ["bb", "cc"], "d", [("eee"), ["ffff"], "ggg"])
print(our_tuple[1])
print(our_tuple[1][1])

# posebnost
temp = (1,2,[1,2,3])
print(temp,type(temp))
temp[2][0] = 5
print(temp)
print()


# Naloga
# Izpišite zadnjih 5 števil
our_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(our_tuple[-5:])
#print(our_tuple[-2:-5:-2])

#https://collabedit.com/5ew4g