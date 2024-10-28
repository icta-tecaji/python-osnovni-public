barve = ("rdeča", "zelena", "modra", "rumena", "črna", "bela")

print(barve, type(barve))

# Tuples are ordered
t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(t1 == t2)

# Tuples can contain any arbitrary object
# Values in tuples are accessed through index
print(barve[1])

# Tuples are IMMUTABLE
# barve[2] = "oranžna"


moja_vrednost = (5,)  # pri enem elementu moramo dodati vejico

# Primer uprabe tuple
# tuple unpacking
a = 5
b = 10

a, b = b, a
print(a, b)
