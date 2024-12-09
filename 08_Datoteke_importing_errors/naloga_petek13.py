## Naloga Petek 13-ti:

# Napišite funkcijo, ki v datoteko naloga_petek13.txt zapiše vse datume, ki so petek 13. v letih od 2020 do (brez) 2030.
# Da najdete datume si lahko pomagate s knjižnjico datetime.

from datetime import date

# print(help(date))

def funkcija():
    with open("naloga_za_petek_13.txt", "w") as f:
        for leto in range(2020, 2030):
            for mesec in range(1, 13):
                datum = date(leto, mesec, 13)
                if datum.weekday() == 4:
                    # 13. Mes YYYY
                    f.write(f'{datum.strftime("%d. %b %Y")}\n')
                    
funkcija()
