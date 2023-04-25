# Ustvarimo spremenljivko v katero shranimo besedo
beseda = "lokomotiva"
print(f"Iskana beseda je: {beseda}")
# Definiramo koliko ugibov
n = 10
counter = 0

while counter < n:
    # 2. Izpisal _ _ _ _ _ _ _

    # 3. Uporabnik naj vnese neko črko
    ugib = input("Vnesi ugibano črko: ")
    print(f"Ugibal je črko {ugib}")

    # 4. Preverimo ali je črka del besede
    if ugib in beseda:
        print("Pravilna črka")
    else:
        print("Nepravilna črka")
        counter += 1

    # 5. Preverimo ali je igralec uganil celotno besedo

    # 5a. Če je uganil je zmagal. Konec igre

    # 5b. Če ni ugnil in nima več ugibo je izgubil. Konec igre

    # 5c. Če ni ugainl besede in ima še ugibov gremo nazaj na korak - 2
    