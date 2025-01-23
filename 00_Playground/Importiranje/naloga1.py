# Naloga:
# Ustvarite nov modul imenovan <b>naloga1.py</b>. Znotraj modula napišite funkcijo <b>pretvornik(x, mode)</b>,
# ki spreminja radiane v stopinje in obratno.

# Funkcija naj sprejme 2 argumenta. Prvi argument je vrednost, katero želimo pretvoriti. Drugi argument,
# imenovan <b>mode</b> pa nam pove v katero enoto spreminjamo.

#     mode = "deg2rad" pomeni, da spreminjamo iz stopinj v radiane
#     mode = "rad2deg" pomeni, da spreminjamo iz radianov v stopinje

# Za pomoč pri pretvarjanju uporabite <b>math</b> modul.

# Zravn modula prilepite podano skripto <b>test.py</b> in to skripto zaženite.

import math


def pretvornik(x, mode):
    if mode == "deg2rad":
        return math.radians(x)
    if mode == "rad2deg":
        return math.degrees(x)


if __name__ == "__main__":
    pass
