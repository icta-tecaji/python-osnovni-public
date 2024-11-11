# def funkcija_1(x, y, z): # x, y, z are parameters
#     print(f"X vrednost: {x}")
#     print(f"Y vrednost: {y}")
#     print(f"Z vrednost: {z}")

# funkcija_1(1, 2, 3) # 1, 2, 3 are arguments
# print()
# funkcija_1(3, 2, 1) # 1, 2, 3 are arguments

# funkcija_1(1,2)


# NALOGA

# Napiši funkcijo, ki sprejme 3 argumente.
# Funkcija naj izpiše kateri ima največjo vrednost in koliko je ta vrednost.

# Primeri:

# Input:
# fun_01(0,-5,6)

# Output:
# Tretji argument je največji. Vrednost: 6

# Input:
# fun_01(1, 50, -50)

# Output:
# Drugi argument je največji. Vrednost: 50


def fun_01(x, y, z):
    # preveri če je X največji
    if x >= y and x >= z:
        print(f"Prvi argument je največji. Vrednost: {x}")
        # preveri če je Y največji
    if y >= x and y >= z:
        print(f"Drugi argument je največji. Vrednost: {y}")
        # preveri če je Z največji
    if z >= x and z >= y:
        print(f"Tretji argument je največji. Vrednost: {z}")


fun_01(0, -5, 6)
fun_01(1, 50, -50)
fun_01(1, 1, 1)
