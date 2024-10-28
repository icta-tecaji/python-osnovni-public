stevilke = [1, 2, 3, 4, 5, 6, 7]

for stevilka in stevilke:
    if stevilka % 2 == 0:
        print(stevilka)
    print("Izvajam zanko")


cene_brez_ddv = [100, 200, 300, 400, 500]
cena_z_ddv = []

for cena in cene_brez_ddv:
    cena_z_ddv.append(cena * 1.22)

print(cena_z_ddv)

# Klasičen for loop z range
for i in range(5, 50, 5):
    print(i)
