barve = ["rdeča", "modra", "zelena", "rumena", "črna", "bela"]
print(barve, type(barve))

# Lists are ordered -> To pomeni, da so podatki shranjenji v list v določenem zaporedju in ostanejo v tem zaporedju.
a = [1, 2, 3]
b = [3, 2, 1]
print(a == b)

# Lists Can Contain Arbitrary Objects -> Za podatke v list-u ni potrebno, da so istega tipa (data type).
c = [1, 3.45, "Python", True, None]
print(c)

# List Elements Can Be Accessed by Index
print(barve[1])
print(barve[4])
print(barve[-1])

# Slicing Lists -> Slicing je način kako dostopamo do več elementov v list-u.
print(barve[1:4])
print(barve[:4])
print(barve[3:])

print(barve[-3:])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1:8:2])
# Zamenjat vrstni red elementov v list-u
print(numbers[::-1])

# Lists can be nested to arbitrary depth
moj_list = ["zelena", "rdeča", [1, 2, 3, 4], "rumena"]
print(moj_list[2][3])

# Lists Are Mutable
moj_list[2] = "modra"
print(moj_list)

# Adding Elements to a List
moj_list.append("črna")
print(moj_list)

temp = moj_list[0]
moj_list[0] = moj_list[1]
moj_list[1] = temp
print(moj_list)

# extend() -> Metoda, ki doda več elementov v list.
moj_list.extend(["rjava", "roza"])
print(moj_list)
# insert() -> Metoda, ki doda element na določeno mesto v list.
moj_list.insert(2, "vijolična")
print(moj_list)

# Removing Elements from a List
# remove() -> Metoda, ki odstrani element iz list-a.
moj_list.remove("rjava")
print(moj_list)

# pop() -> Metoda, ki odstrani element iz list-a na določenem mestu.
moj_list.pop(2)
print(moj_list)

# element v listu
print("modra" in moj_list)
