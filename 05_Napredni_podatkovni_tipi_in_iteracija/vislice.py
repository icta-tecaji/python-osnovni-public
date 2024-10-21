"""Igra vislice napisana v Pythonu."""

# Ustvarimo spremenljivko v katero shranimo iskano besedo
# TODO: Dodaj seznam besed katere se naključno izberejo
iskana_beseda = "lokomotiva"
MAKSIMALNO_STEVILO_NAPAK = 5
trenutno_stevilo_napak = 0

trenutne_napcne_crke = ""

print("***** Pozdravljeni v igri vislice! *****")

while trenutno_stevilo_napak < MAKSIMALNO_STEVILO_NAPAK:
    # 1. Izpišemo _ _ _ _ _ _ (in dodamo katere črke so bile že uganjene)

    # 2. Uporabnik ugiba črko
    ugibana_crka = input("Vnesi ugibano črko: ")
    print(f"Uporabnik je vnesel črko: {ugibana_crka}")

    # 3. Preverimo če je črka v besedi
    if ugibana_crka in iskana_beseda:
        print("Pravilna črka!")
    else:
        trenutne_napcne_crke += ugibana_crka
        print(f"Napačna črka! Napačne črke: {trenutne_napcne_crke}")
        trenutno_stevilo_napak += 1

    # 4. Preverimo ali je uporabnik uganil iskano besedo
    # 4a. Če je uporabnik uganil besedo je zmagal in je igre konec
    # 4b. Če uporabnik ni uganil besede in ima še poskusov, se vrne na korak 1
    # 4c. Če uporabnik ni uganil besede in nima več poskusov, je izgubil in je igre konec
