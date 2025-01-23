# importiranje

# MODULE --> je datoteka ki se konča s *.py
# PACKAGE --> je direktorij ki vsebuje vsaj en module


# import math

# import moj_modul


# moj_modul.izpisi_stevilko_100()

# print()
# print()
# print()
# print(math.log(5.7825))
# print(math.log(144, 12))

# import moduli_package
# import moduli_package.nov_module
# import moduli_package.nov_module2
# import moduli_package.nov_module3

# print()
# moduli_package.nov_module.fun()
# moduli_package.nov_module2.fun()
# moduli_package.nov_module3.fun()


# print()
# print(dir(moduli_package.nov_module3))


# fido = moj_modul.Pes("Fido", 6)

# print()
# print(fido)
# print(type(fido))
# fido.lajaj()

# import moj_modul as mm

from moj_modul import *

# from moj_modul import Pes, izpisi_stevilko_100, nekineki

print()
izpisi_stevilko_100()

fido = Pes("Fido", 5)
fido.lajaj()

nekineki()


# Naloga:
# Napišite funkcijo, ki v datoteko <i>naloga_petek13.txt</i> zapiše vse datume,
# ki so <b>petek 13.</b> v letih od 2020 do (brez) 2030.

# Da najdete datume si lahko pomagate s knjižnjico datetime.

import datetime

# x = datetime.date(2020, 1, 1)
# datetime.date().weekday()
# print(x.strftime("%d. %b %Y"))


def petek13():
    with open("naloga_petek13.txt", "w") as file:
        for leto in range(2020, 2030):
            for mesec in range(1, 13):
                datum = datetime.date(leto, mesec, 13)
                if datum.weekday() == 4:
                    file.write(f"{datum.strftime('%d. %b %Y')}\n")
                else:
                    pass


petek13()


# ```python
# 13. Mar 2020
# 13. Nov 2020
# 13. Aug 2021
# 13. May 2022
# 13. Jan 2023
# 13. Oct 2023
# 13. Sep 2024
# 13. Dec 2024
# 13. Jun 2025
# 13. Feb 2026
# 13. Mar 2026
# 13. Nov 2026
# 13. Aug 2027
# 13. Oct 2028
# 13. Apr 2029
# 13. Jul 2029
# ```
