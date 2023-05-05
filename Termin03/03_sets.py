# SETS
# s = {"medved", "zajec", "volk", "los", "los"}
# print(s)
# print(type(s))

## Elements in sets must be immutable
# s = {42, "eee", 3.45, (1,2)}
# s = {1,2,3,4, [1,2,3]} # error - elements must be immutable
# print(s)
# print(type(s))

## Sets are unordered
# s = {1,2,3,4,5,6,7,8,9}
# print(s)
# print(type(s))

# Operations on sets
x1 = {1, 2, 3, 4}
x2 = {4, 5, 6, 7}

## Union
#x3 = x1.union(x2)
#print(x3)

## Intersection
# x3 = x1.intersection(x2)
# print(x3)

## Difference
# x3 = x2.difference(x1)
# print(x3)

## Symetric difference
# x3 = x1.symmetric_difference(x2)
# print(x3)

# Modifying sets
# x = {1,2,3,4}
# x.add("nov_element")
# x.add(1)
# print(type(x), x)

# x = {1,2,3,4}
# x.remove(3)
# x.remove(6)
# print(x)

# x = {1,2,3,4}
# x.discard(3)
# x.discard(6)
# print(x)

# x = {1,2,3,4, 5, 6, 7, 8, 9, 0, -1}
# y = x.pop()
# print("Popped", y)
# print(x)

x = {1,2,3,4, frozenset((3,4,5))}
print(x)