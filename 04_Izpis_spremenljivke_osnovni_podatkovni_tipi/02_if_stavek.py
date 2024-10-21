# print("Začetek programa")
# temperatura = 22
# MAX_TEMPERATURA = 25

# if temperatura > MAX_TEMPERATURA:
#     print("Pogoj je izpolnjen.")
#     print("ALARM!!!")

#     # Koda znotraj if stavka
#     print("Izvajam kodo znotraj if stavka.")
# elif temperatura == MAX_TEMPERATURA:
#     print("Temperatura je enaka MAX_TEMPERATURI.")
#     print("Pošiljam opozorilo.")
# else:
#     print("Pogoj ni izpolnjen.")
#     print("Vse je v redu.")

# print("Konec programa")

stevilo_01 = int(input("Vnesi prvo število: "))
stevilo_02 = int(input("Vnesi drugo število: "))

if stevilo_01 > stevilo_02:
    print(f"Število {stevilo_01} je večje od števila {stevilo_02}.")
elif stevilo_01 == stevilo_02:
    print(f"Število {stevilo_01} je enako številu {stevilo_02}.")
else:
    print(f"Število {stevilo_01} je manjše od števila {stevilo_02}.")
