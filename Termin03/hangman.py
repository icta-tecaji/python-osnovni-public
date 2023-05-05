# Ustvarimo spremenljivko v katero shranimo besedo
beseda = "lokomotiva"
print(f"Iskana beseda je: {beseda}")
# Definiramo koliko ugibov
n = 10
won = False
ugibi = []

word_check = {}
for ch in beseda:
    word_check[ch] = False

for i in range(n):
    # 2. Izpisal _ _ _ _ _ _ _
    izpis = ""
    for ch in beseda:
        if ch in ugibi:
            izpis += f"{ch} "
        else:
            izpis += "_ "
    print(izpis)

    # 3. Uporabnik naj vnese neko črko
    print()
    print(f"{i+1} / {n} ugibi")
    print(f"Dosedanji ugibi: {ugibi}")

    ugib = input("Vnesi ugibano črko: ")
    print(f"Ugibal je črko {ugib}")
    ugibi.append(ugib)

    # 4. Preverimo ali je črka del besede
    if ugib in beseda:
        print("Pravilna črka")
        word_check[ugib] = True
    else:
        print("Nepravilna črka")

    # 5. Preverimo ali je igralec uganil celotno besedo
    # 5a. Če je uganil je zmagal. Konec igre
    if False in word_check.values():
        won = False
    else:
        won = True
        break

    # 5b. Če ni ugnil in nima več ugibo je izgubil. Konec igre
    # 5c. Če ni ugainl besede in ima še ugibov gremo nazaj na korak - 2
    
if won:
    print("ZMAGA")
else:
    print("Poraz")