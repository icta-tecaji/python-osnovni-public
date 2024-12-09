# # Naloga 05
# **Točke: /5**

# Napišite razred `Planet`. Ko ustvarimo novo instanco razreda, vanj shranimo ime, razdaljo od sonca in maso planeta.

# Planet naj ima tudi funkcijo `razdalja_od_planeta`, ki kot argument prejme še en drugi planet. Funkcija naj izračuna kolikšna je razdalja med planetoma.


# Napišite tudi razred `Osoncje`. Ko ustvarimo novo instanco razreda lahko kot argument pošljemo list planetov ali pa tudi ne.

# Osončje naj ima spremenljivko `planeti`, ki je list planetov, ki se nahajajo v osončju.

# Osončje naj ima funkcijo `dodaj_planet`, ki kot argument prejme planet in le-tega doda v svoj list planetov.

# Osončje naj ima funkcijo `planet_z_najvecjo_maso`, ki naj vrne ime planeta z najvecjo maso.

# Osončje naj ima funkcijo `razvrsti_po_oddaljenosti`, ki naj planete razvrsti od najblizjega do najblj oddaljenega planeta. Nato naj funkcija vrne list samo imen planetov v pravilnem vrstnem redu.

# ```python
# venera = Planet("Venera", 108_000_000, 40.8685)
# zemlja = Planet("Zemlja", 152_000_000, 59.742)
# uran = Planet("Uran", 19_000_000_000, 868)

# print(zemlja.razdalja_od_planeta(venera))
# OUTPUT:
# 44000000


# print(zemlja.razdalja_od_planeta(uran))
# OUTPUT:
# 18848000000


# mars = Planet("Mars", 227_000_000, 6.4185)
# jupiter = Planet("Jupiter", 816_000_000, 18980)

# osoncje = Osoncje(planeti=[venera, zemlja, uran, mars, jupiter])

# print(osoncje.razvrsti_po_oddaljenosti())
# OUTPUT:
# ['Venera', 'Zemlja', 'Mars', 'Jupiter', 'Uran']


# saturn = Planet("Saturn", 1_513_000_000, 5684)
# merkur = Planet("Merkur", 68_000_000, 3.3022)
# neptun = Planet("Neptun",  30_000_000_000, 102)

# osoncje.dodaj_planet(saturn)
# osoncje.dodaj_planet(merkur)
# osoncje.dodaj_planet(neptun)

# print(osoncje.razvrsti_po_oddaljenosti())
# OUTPUT:
# ['Merkur', 'Venera', 'Zemlja', 'Mars', 'Jupiter', 'Saturn', 'Uran', 'Neptun']

# print(osoncje.planet_z_najvecjo_maso())
# OUTPUT:
# Jupiter
# ```