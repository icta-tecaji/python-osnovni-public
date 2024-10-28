# Set elements are unique. Duplicate elements are not allowed
stevilke = {1, 2, 3, 4, 5, 5}  # noqa: B033
print(stevilke, type(stevilke))

# Sets are unordered
set_01 = {1, 2, 3}
set_02 = {3, 2, 1}
print(set_01 == set_02)

# Sets do not support indexing, slicing, or other sequence-like behavior.

# Elementi so lahko poljubni ampak morajo biti "immutable."
print({1, 2.33, "ffrfr", True, (1, 2, 3)})

# operacije z množicami
x1 = {1, 2, 3, 4}
x2 = {3, 4, 5, 6}

print(x1.union(x2))
print(x1.intersection(x2))
print(x1.difference(x2))
print(x2.difference(x1))

print(1 in x1)

# Modifying Sets
# add() -> Metoda, ki doda element v set.
x1 = {1, 2, 3, 4}
x1.add(5)
print(x1)

# remove() -> Metoda, ki odstrani element iz set-a.
x1.remove(2)
print(x1)
# x1.remove(2)  # KeyError: 2
x1.discard(2)  # ne vrne napake če elementa ni v set-u

# odstranjevanje podvojenih elementov
stevilke = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2]
unique_stevilke = list(set(stevilke))
print(unique_stevilke)
