"""Igra vislice napisana v Pythonu."""

import random

# Ustvarimo spremenljivko v katero shranimo iskano besedo
BAZEN_BESED = {
    "avtomobil",
    "lokomotiva",
    "kolo",
    "motor",
    "letalo",
    "vlak",
    "ladija",
    "helikopter",
    "kombi",
    "tovornjak",
    "bus",
    "kamion",
    "skuter",
    "moped",
    "taksi",
    "avtobus",
    "tramvaj",
    "kolesar",
    "pešec",
    "voznik",
    "potnik",
    "pilot",
    "kapitan",
    "strojevodja",
    "bolnišnica",
    "šola",
    "vrtec",
    "univerza",
    "fakulteta",
    "gimnazija",
    "trgovina",
    "restavracija",
    "kavarna",
    "bar",
    "diskoteka",
    "klub",
    "gostilna",
    "picerija",
    "muzej",
    "knjižnica",
    "galerija",
    "zoo",
    "akvarij",
    "cirkus",
    "gledališče",
    "kino",
    "koncert",
    "festival",
    "razstava",
    "predstava",
    "film",
    "glasba",
    "ples",
}

iskana_beseda = random.choice(list(BAZEN_BESED))
MAKSIMALNO_STEVILO_NAPAK = 8
trenutne_napcne_crke = []

# Ustvarimo slovar v katerem bomo shranjevali preverjanje črk
preverjanje_besede = {}
for crka in iskana_beseda:
    preverjanje_besede[crka] = False

print("***** Pozdravljeni v igri vislice! *****")

while len(trenutne_napcne_crke) <= MAKSIMALNO_STEVILO_NAPAK:
    print()
    # 1. Izpišemo _ _ _ _ _ _ (in dodamo katere črke so bile že uganjene)
    izpis = ""
    for crka in iskana_beseda:
        pravilne_crke = [crka for crka, je_uganjena in preverjanje_besede.items() if je_uganjena]
        if crka in pravilne_crke:
            izpis += crka
        else:
            izpis += "_"
        izpis += " "
    print(f"TRENUTNO STANJE: {izpis.upper()}")

    # 2. Uporabnik ugiba črko
    ugibana_crka = input("Vnesi ugibano črko: ")
    # VALIDACIJA: Preverimo če je uporabnik vnesel samo eno črko
    if len(ugibana_crka) != 1 or not ugibana_crka.isalpha():
        print("Vnesi samo eno črko!")
        continue

    # 3. Preverimo če je črka v besedi
    if ugibana_crka in iskana_beseda:
        print("Pravilna črka!")
        preverjanje_besede[ugibana_crka] = True
    elif ugibana_crka not in trenutne_napcne_crke:
        trenutne_napcne_crke.append(ugibana_crka)
        # 4c. Če uporabnik ni uganil besede in nima več poskusov, je izgubil in je igre konec
        if len(trenutne_napcne_crke) > MAKSIMALNO_STEVILO_NAPAK:
            print()
            print(f"Žal ste porabili vse poskuse. Iskana beseda je bila {iskana_beseda.upper()}")
            break
        print(
            f"Napačna črka {len(trenutne_napcne_crke)}/{MAKSIMALNO_STEVILO_NAPAK} -> Napačne črke: {", ".join(trenutne_napcne_crke)}",
        )
    else:
        print("Črka je že bila uporabljena!")

    # 4. Preverimo ali je uporabnik uganil iskano besedo
    if False in preverjanje_besede.values():
        # 4b. Če uporabnik ni uganil besede in ima še poskusov, se vrne na korak 1
        continue
    else:
        # 4a. Če je uporabnik uganil besedo je zmagal in je igre konec
        print(f"Čestitke, uganili ste besedo {iskana_beseda}!")
        break
