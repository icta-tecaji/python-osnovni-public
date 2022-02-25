# Set

# prej: list(), tuple(), dict()
# sedaj: set()

# dict --> { <key1>:<value1>, <key2>:<value2>,...}
# set --> { <key1>, <key2>,...}
a = {}
b = set({})
print(a, type(a))
print(b,type(b))
print()


s = {42, "eee", (1,2,3), 3.14159}
print(s)
print()

#s = {42, "eee", [1,2,3], 3.14159} # --> Type Error
#print(s)
#print()

s = {42, "eee", (1,2,3,(1,2,3,4)), 3.14159}
print(s)
print()

x1  ={1,2,3,4}
x2 = {4,5}
x3 = {5,6}
x4 = {9,10}

# unija (union)
x = x1.union(x2)
print(x)
print(type(x))
print()
print(x1 | x2) # AltGr + w = |
print()

x = x1.union(x2,x3,x4)
print(x)
print(x1 | x2 | x3 | x4)
print()



# presek (intersection)
x = x1.intersection(x2)
print(x)
print(x1 & x2)
print()

x = x1.intersection(x2,x3,x4)
print(x)
print(x1 & x2 & x3 & x4) # shift + 6 = &
print()


# razlika (difference)
x = x1.difference(x2)
print(x)
print(x1 - x2) # minus
print()

x = x1.difference(x2,x3,x4)
print(x)
print(x1 - x2 - x3 - x4)
print()

# simetrična razlika (symmetric_difference)
x = x1.symmetric_difference(x2)
print(x)
print(x1 ^ x2) # AltGr + 3 = ^
print()

# x = x1.symmetric_difference(x2,x3,x4) # --> Error
# print(x)
# print(x1 ^ x2 ^ x3 ^ x4) # AltGr + 3 = ^
# print()

a = {1,2,3,4}
a.add("nekineki")
print(a)
print()

a.remove(3)
print(a)

# a.remove(6) # --> KeyError
#print(a)

a.discard(6) # --> enako kot remove, samo da ne vrže Keyerror
print("prišel do tukaj")
print(a)
a.discard(2)
print(a)
print()

x = a.pop()
print(f"First pop: {x}\nSet:{a}\n")
x = a.pop()
print(f"Secound pop: {x}\nSet:{a}\n")
x = a.pop()
print(f"Third pop: {x}\nSet:{a}\n")
#x = a.pop() # --> KeyError
#print(f"Fourth pop: {x}\nSet:{a}\n")

a = {1,2,3,4,"nekineki"}
a = set({})
print(a)
a = {1,2,3,4,"nekineki"}
a.clear()
print(a)
print()


x = frozenset([1,2,3,4]) # immutable set --> se ga ne da spreminajti
print(x)
print(type(x))
print()

# x.add(5) # AtributeError

a = x.union({4,6,7})
print(a)
print()

temp_set = set(x)
print(temp_set)
temp_set.add(10)
print(temp_set)
print()


# Naloga
# Iz sledečega lista odstranite vrednost, ki se nahaja na indexu 4. Vrednost dodajte v dictionary pod ključ d.
# Nato iz dictionary pridobite vse vrednosti. Te vrednosti shranite v nov set in novonastali set primerjajte ali je enak podanemu set-u.

our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_set = {357, 12, 12, 8, 5, 2, 2}


x = our_list.pop(4)
our_dict["d"] = x
# our_dict["d"] = our_list.pop(4)

vse_vrednosti = our_dict.values()

vse_vrednosti_set = set(vse_vrednosti)

print(vse_vrednosti_set == our_set)



# Naloga
# Izpišite vse skupne črke sledečih dveh stringov.
str1 = "Danes je lep dan"
str2 = "Jutri bo deževalo"

str1_set = set(str1)
str2_set = set(str2)

common = str1_set.intersection(str2_set)
print(common)




























