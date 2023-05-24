# Naloga: ¶
# Ustvarite razred Vozilo. Vsaka instanca naj
# ima svojo specifično hitrost in kilometrino.
# Izpišite njegove lastnosti na sledeč način:
# "Max hitrost vozila: -hitrost-.
# Prevozenih je -kilometrina- km."

# Primeri:
# Input:
# avto = Vozilo(300, 80)
# Output:
# Max hitrost vozila: 300. Prevozenih je 80 km.

# Input:
# motor = Vozilo(180, 33)
# Output:
# Max hitrost vozila: 180. Prevozenih je 33 km.


class Vozilo:
    def __init__(self, hitrost, km):
        self.hitrost = hitrost
        self.kilometrina = km


avto = Vozilo(300, 80)
print(f"Max hitrost vozila: {avto.hitrost}. Prevozenih je {avto.kilometrina} km.")

motor = Vozilo(180, 33)
print(f"Max hitrost vozila: {motor.hitrost}. Prevozenih je {motor.kilometrina} km.")
