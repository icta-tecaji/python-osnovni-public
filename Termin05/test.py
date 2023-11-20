# a = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# #print("A = ",a)

# b = a[1]
# print("B = ", b)

# c = b[1]
# print("C = ", c)

# d = c[1]
# print("D = ", d)
# e = d[1]
# print("E = ", e)

#print("Če vse združimo = ",a[1][1][1])


# d = {1: 'a',
#       2.3: 'b', 
#       "string": 'c', 
#       (1,"touple"):'d'}

# print(d)
# print(d[2.3])
# print(d[(1, "touple")]) #touple je kot seznam, le da je nespremenljiv


# i = True
# while True:
#     print(f'Ponovlje')

# prastevila = [2, 3, 5, 7, 11] 
# for prastevilo in prastevila:
#     print(f'{prastevilo} je praštevilo.')


# avti = ["ok", "ok", "ok", "slab", "ok"]

# for avto in avti:
#     if avto == "slab":
#         print("Avto je zanič.")
#         #continue #zakomentiraj continue, da vidiš razliko v delovanju kode
#     elif avto == "ok":
#         print("Avto je ok.")
#     print()
# print("Konec")

# Primer: Filtriranje elementov
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [x**2 for x in a if x%2 == 0 and x%3==0] # multiple ifs
print(a)
print(even_squares)

#Isti način s for zanko

rezutlat=0
for element in a:
    if element%2 == 0 and element%3==0:
        rezutlat=element**2


help(str.split)