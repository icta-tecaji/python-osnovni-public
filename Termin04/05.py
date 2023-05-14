
# Naloga:

# Napiši funkcijo, ki sprejme 3 argumente.

# Funkcija naj izpiše kateri ima največjo vrednost
# in koliko je ta vrednost.

def funkcija_01(a,b,c):
    if a>b and a>c:
        print(f"Prvi argument je največji. Vrednost: {a}")
    if b>a and b>c:
        print(f"Drugi argument je največji. Vrednost: {b}")
    if c>a and c>b:
        print(f"Tretji argument je največji. Vrednost: {c}")

funkcija_01(1,2,3)
funkcija_01(9,2,30)
funkcija_01(1,289,3)
