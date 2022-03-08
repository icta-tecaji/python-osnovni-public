def moj_range(n):
    print("Starting moj generator")
    while n<10:
        yield n
        n += 1
    print("Stop generator")

val = moj_range(5)
print(val)
print(type(val))

# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))

def moj_range(n, m, step=1):
    while n<m:
        yield n
        n += step

for i in moj_range(0, 10):
    print(i)

x = list(moj_range(0, 10))
print(x)
print(type(x))