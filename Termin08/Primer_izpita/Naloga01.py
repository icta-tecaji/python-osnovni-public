# Naloga 01
# Točka: / 5

# Napišite funkcijo funkcija01, ki kot prvi parameter sprejme višino valja in 
# kot drugi parameter sprejme radij valja. Funkcija naj vrne izračunano 
# prostornino valja (lahko privzamete, da so vse volumenske enote v 
# centimetrih in da je izhod v kubičnih centimetrih).

# "π" najdete v built-in knjižnjici math.

# import math
# print(math.pi)
# INPUT:
# funkcija01(2, 3)


# OUTPUT:
# 56.54866776

# REŠITEV:
# Rešitev 
import math

def funkcija01(visina,radij):
    return math.pi*(radij**2)*visina

funkcija01(2, 3)

# ======================================
# ======================================
# ======================================
