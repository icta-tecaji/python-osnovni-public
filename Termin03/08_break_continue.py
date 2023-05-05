# BREAK

# for i in range(10):
#     print("i = ", i)
#     if i >= 5:
#         break
#     print("i**2 = ", i**2)
# print("Nadaljevaje programa")

# CONTINUE
# for i in range(10):
#     print("i = ", i)
#     if i >= 5:
#         continue
#     print("i**2 = ", i**2)
# print("Nadaljevaje programa")

# Naloga:
# Poiščite vsa praštevila med 2 in 30.

# 2 JE praštevilo!
# 3 JE praštevilo!
# 5 JE praštevilo!
# 7 JE praštevilo!
# 11 JE praštevilo!
# 13 JE praštevilo!
# 17 JE praštevilo!
# 19 JE praštevilo!
# 23 JE praštevilo!
# 29 JE praštevilo!
for num in range(2, 31):
    prime = True
    for i in range(2, num):
        if (num%i == 0):
            # print("Ni praštevilo", num)
            prime = False
            break
    if prime:
        print(f"{num} je praštevilo")
        