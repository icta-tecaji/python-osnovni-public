# For loop

# for <var> in <iterable>:
#     <statement>

# <next_block>

# primes = [2, 3, 5, 7, 11] # iterable
# for i in primes:
#     print(i)

# print("Nadaljevanje")

# starosti = (3, 7, 12)
# for age in starosti:
#     print(age, age*12)
# print("Nadaljevanje programa")

# x = range(-5, 10, 1)
# print(list(x))

# for i in range(10):
#     print(i)

# pets = {
#     "macka": 6,
#     "pes": 12,
#     "krava": 20
# }
# print(list(pets.items()))
# for pet, year in pets.items():
#     print(f"{pet} je star/a {year} let.")

# for key in pets.keys():
#     print(key, pets[key])


# BREAK
# avti = ["ok", "ok", "ok", "slab", "ok"]

# for avto in avti:
#     print(avto)
#     if avto == "slab":
#         print("Avto je zanič")
#         break
#     print("Naslednji avto...")
# print("Nadaljevanje programa")

avti = ["ok", "ok", "ok", "slab", "ok"]

# CONTINUE
# for avto in avti:
#     print(avto)
#     if avto == "slab":
#         print("Avto je zanič")
#         continue
#     print("Naslednji avto...")
# print("Nadaljevanje programa")



# VAJA
# Iz danega dictionary izpišite vse ključe, 
# katerih vrednost vsebuje črko **r**.
# https://collabedit.com/j4snu
d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}


# for key, value in d.items():
#     if "r" in value:
#         print(key)


# Poiščite vsa praštevila med 2 in 30.
# Rešitev
# for num in range(2, 31):
#     #print("Num = ",num)
#     prime = True
#     for i in range(2, num):
#         #print("Preveri ostanek :", num, "/", i)
#         if num%i == 0:
#             #print("To NI praštevilo")
#             prime = False
#             break
#     if prime:
#         print(f"{num} JE praštevilo")
