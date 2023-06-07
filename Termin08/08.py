# Naloga:
# Napišite funkcijo, ki v datoteko naloga_petek13.txt
# zapiše vse datume, ki so petek 13. v letih od 2020 do (brez)
# 2030.
# Da najdete datume si lahko pomagate s knjižnjico datetime.

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

from datetime import date


def funkcija():
    with open("naloga_petek13.txt", "w") as f:
        for year in range(2020, 2030):
            for month in range(1, 13):
                datum = date(year, month, 13)
                if datum.weekday() == 4:
                    f.write(datum.strftime("%d. %b %Y") + "\n")
                    print("Petek", datum)


funkcija()
