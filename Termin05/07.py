# variable scope

# x = 5

# def fun():
#     # global x
#     # print(x)
#     x = 3
#     print(x)

# fun()
# print(x)

# spr1 = 5
# print(f"Spr1: {spr1}")

# def funkcija(spr1):
#     print(f"Spr1: {spr1}")
    
# funkcija(100)
# print(f"Spr1: {spr1}")

# def funkcija(l):
#     print(l)
#     l[0] = 100

# seznam = [3, 7, 13]
# funkcija(seznam)
# print(seznam)
a = 5
def fun():
    # global a
    a = 3
    return a
fun()    
print(a)
