# Keyword arguments
# def pozdrav(naslavljanje, ime="Nejc", priimek="Pavliha"):
# 	print(f"Pozdravjeni {naslavljanje} {ime} {priimek}")

# def pozdrav(naslavljanje, ime, priimek):
# 	print(f"Pozdravjeni {naslavljanje} {ime} {priimek} !!!!")

# pozdrav("gospod","Anže","Glušič")
# print()
# pozdrav(ime="gospod",priimek="Anže",naslavljanje="Glušič")
# print()
# pozdrav(ime="Anže",priimek="Glušič",naslavljanje="gospod")

# pozdrav("gospod","Anže","Glušič")
# pozdrav("gospod",priimek="Novak")

# Naloga

# Napišite funkcijo, ki izpiše prvih N največjih vrednosti v podanem listu.
# Funkcija naj ima dva parametra.
# Prvi parameter je list, znotraj katerega bomo iskali največje vrednosti.
# Drugi parameter število, ki nam pove koliko prvih največjih števil naj izpišemo.
# Če vrednost ni podana, naj se izpiše prvih 5 največjih števil.


# x = max([1,2,3,7,0,11,4]) # rezultat tega je, (x=11)
# x =[1,2,3]
# x.remove(2)
# print(x)


def vaja(l, N=5):
    for i in range(N):
        max_number = max(l)
        l.remove(max_number)
        print(max_number)

    # l = sorted(l,reverse=True)
    # print(l[:N])

    # max
    # remove


vaja([1, 5, 7, -2, 3, 8, 2, -5, 12, -22])
print()
vaja([1, 5, 7, -2, 3, 8, 2 - 5, 12, -22], 3)


# Primeri:

# Input:
# vaja([1,5,7,-2,3,8,2-5,12,-22])

# Output:
# 12
# 8
# 7
# 5
# 3

# Input:
# vaja([1,5,7,-2,3,8,2-5,12,-22], 3)

# Output:
# 12
# 8
# 7
