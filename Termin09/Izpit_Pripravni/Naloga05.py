# # Naloga 05
# **Točke: /5**

# Napišite razred `Volk`. Ko ustvarimo novo instanco
# razreda, vanj shranimo ime in njegovo hitrost.

# Napišite tudi razred `Trop`. Ko ustvarimo novo
# instanco razreda lahko kot argument pošljemo list volkov v tropu ali pa tudi ne.

# Trop naj ima spremenljivko `volkovi`, ki je list
# volkov, ki se nahajajo v tropu.

# Trop naj ima funkcijo `dodaj_volka`, ki kot argument
# prejme instanco razreda Volk in le-tega doda v svoj list volkov.

# Trop naj ima funkcijo `najhitrejsi_volk`, ki naj vrne
# ime najhitrejšega volka.

# Trop naj ima funkcijo `razvrsti_po_hitrosti`, ki
# naj volkove razvrsti od najpočasnejšega do najhitrejšega.
# Nato naj funkcija vrne list samo imen volkov v pravilnem vrstnem redu.

# ```python
# rex = Volk("Rex", 51)
# milo = Volk("Milo", 55)
# leo = Volk("Leo", 59)

# trop = Trop([rex, milo, leo])
# print(trop.najhitrejsi_volk())
# OUTPUT:
# Leo

# chip = Volk("Chip", 49)
# bruce = Volk("Bruce", 62)

# trop.dodaj_volka(chip)
# trop.dodaj_volka(bruce)
# print(trop.najhitrejsi_volk())
# OUTPUT:
# Bruce


# print(trop.razvrsti_po_hitrosti())
# OUTPUT:
# ['Chip', 'Rex', 'Milo', 'Leo', 'Bruce']
# ```


class Volk:
    def __init__(self, ime, hitrost):
        self.ime = ime
        self.hitrost = hitrost


class Trop:
    def __init__(self, volkovi=[]):
        self.volkovi = volkovi

    def dodaj_volka(self, volk):
        self.volkovi.append(volk)

    def najhitrejsi_volk(self):
        best_wolf = self.volkovi[0]
        for volk in self.volkovi[1:]:
            if volk.hitrost > best_wolf.hitrost:
                best_wolf = volk
        return best_wolf.ime

    def razvrsti_po_hitrosti(self):
        self.volkovi = sorted(self.volkovi, key=filter_)
        return [v.ime for v in self.volkovi]


def filter_(v):
    return v.hitrost


rex = Volk("Rex", 51)
milo = Volk("Milo", 55)
leo = Volk("Leo", 59)

trop = Trop([rex, milo, leo])
print(trop.najhitrejsi_volk())

chip = Volk("Chip", 49)
trop.dodaj_volka(chip)

print(trop.razvrsti_po_hitrosti())
