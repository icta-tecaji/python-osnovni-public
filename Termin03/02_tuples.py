# TUPLES
# t = ("pingvin", "medved", "los", "volk")
# print(type(t))
# print(t)

# Tuples are ordered
# t = ("pingvin", "medved", "los", "volk")
# t2 = ("pingvin", "los", "medved", "volk")
# print(t == t2)

# Tuples can contain arbitrary object
# t = ("pingvin", 1, 2.34, False, 2 +4j)
# print(type(t))
# print(t)

# Values are accessed by index
# t = ("pingvin", "medved", "los", "volk")
# print(t[-1])
# print(t[0])
# print(t[1:3])

# Tuples can be nested
# t = (1, 2, 3, (44, 55, 66))
# print(type(t))
# print(t)
# print(t[-1][1])

# Tuples are IMMUTABLE
# t = ("pingvin", "medved", "los", "volk")
# t[1] = "Koza" # error
# del t[1] # error

# t = (1,2,3,4,5)
t = (3,)
print(type(t), t)