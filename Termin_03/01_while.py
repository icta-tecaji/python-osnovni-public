# 
#Napišite program, ki bo uporabnika uprašal naj vnese 
# neko celoštevilsko vrednost.
#Program naj nato izpiše ali je vrednost deljiva z 3 in z 7, ali ne.

# Rešitev
#x = int(input("Vnesi celo število: "))

#if x%3==0 and x%7==0:
#    print("TRUE")
#else:
#    print("ni deljivo")

#print("nadaljevanje programa")

# i = 0
# while i<10:
#     print(f"Korak {i}")
#     i += 1 #i = i + 1

# print("Nadaljevanje programa")

# temperatura = 15

# while temperatura<20:
#     print("Ogrevanje...")
#     temperatura += 1

# print("Stanovanje je dovolj toplo")

# Vaja 3
# Napišite program, ki izpiše prvih 10 sodih števil.

# x = 0
# i = 0
# while i < 100:
#     if x%2==0:
#         print(x)
#         i += 1
#     x += 1



# VAJA
# Uporabnik naj vnese željeno dolžino Fibonaccijevega 
# zaporedja. Program naj nato to zaporedje shrani v 
# list in ga na koncu izpiše.

# Fibonacci sequence
#[0, 1, 1, 2, 3, 5, ]
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#
#l = [0,1,1]
#l.append(2)
#print(l)
# Rešitev

l = [0, 1]
x = int(input("Vnesi dolzino FIbonaccija: "))

while len(l) < x:
    # najdi novo cifro
    z = l[-1] + l[-2]
    # dodaj novo cifro v l
    l.append(z)

print(l)