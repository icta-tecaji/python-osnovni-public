import random

# Naloga:
# Napišite funkcijo <b>is_palindrom</b>, ki od uporabnika zahteva naj vnese besedo.
# Funkcija naj vrne True, če je beseda palindrom, v nasprotnem primeru False.
# Palindrom je beseda, ki se prebere isto od leve proti desni in od desne proti levi.

# Če uporabnik vnese samo številke naj funkcija rais-a ValueError.

# Program naj 3x zažene funkcijo. V kolikor pride do ValueError naj se izpiše sporočilo in izvajanje programa nadaljuje.


def is_palindrom():
    try:
        beseda = input("beseda: ")
        # if beseda.strip().isnumeric():
        if beseda.strip().isdigit():
            raise ValueError
        return beseda == beseda[::-1]

    except ValueError:
        print("Vnešene so bile samo številke.")
        return False


# for _ in range(3):
#     print(is_palindrom())


# for i in range(len(niz)):
#     if niz[i]==niz[-i-1]

# print(niz == niz[::-1])

# for a, b in zip([1, 2, 3], [5, 6, 7]):  # [(1,5),(2,6),(3,7)]
#     print(a, b)
# for a, b in zip(niz, niz[::-1]):
#     if a != b:
#         print("Ni palindrom")
#         break


# ```python
# OUTPUT:
# Vnesi besedo: Ananas
# The word is NOT palindrom.

# Vnesi besedo: 1234
# Vnešene so bile samo številke.

# Vnesi besedo: racecar
# The word is PALINDROM
# ```


try:
    pass  # koda ki jo probamo izvest
except ValueError:
    pass  # koda ki se izvede če pride do specifično te napake
except:
    pass  # koda ki se izvede v primeru če noben drug except ni pohendlal te zadeve/napke
else:
    pass  # koda ki se izvede v primeru če NE PRIDE do napake
finally:
    pass  # koda ki se izvede v vsakem primeru


class VrednostPremajhna(Exception):
    pass


class VrednostPrevisoka(Exception):
    pass


number = random.randint(-100, 100)

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise VrednostPremajhna
        elif i_num > number:
            raise VrednostPrevisoka
        print("BRAVO! uganil si številko.")
        break
    except VrednostPremajhna:
        print("Ugibana vrednost je premajhna!")
        print()
    except VrednostPrevisoka:
        print("Ugibana vrednost je previsoka!")
        print()
