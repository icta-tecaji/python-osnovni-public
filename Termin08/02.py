# https://shorturl.at/bgsIQ

# Naloga:
# Napišite funkcijo, ki kot parameter x premje neko celo število.
# Funkcija naj izpiše zadnjih x vrstic v datoteki naloga2.txt.
# INPUT:
# funkcija(3)

# OUTPUT:
# line 7
# line 8
# line 9

import os

print("Moj CWD: \t", os.getcwd())


def funkcija(x):
    with open("Termin08/naloga2.txt") as f:
        lines = f.readlines()
        for line in lines[-x:]:
            print(line.strip("\n"))


funkcija(3)
