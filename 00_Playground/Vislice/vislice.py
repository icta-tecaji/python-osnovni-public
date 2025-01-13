# VISLICE (10 ugibanj beseda: "lokomotiva")

# Ustvaril spremenljivke v ketro shranimo besedo katero iščemo
beseda = "lokomotiva"
print(f"Iskana beseda je: {beseda}")

st_ugibanj = 10
ugibi = []

won = False

word_check = {}
for ch in beseda:
    word_check[ch] = False

while st_ugibanj > 0:
    # 1.Izpišemo _ _ _ _ ... (in oddamo katere črke so bile uganjene)
    print()
    # temp = [(el if (el in ugibi) else "_") for el in beseda]
    # print(type(temp), temp)
    # temp = " ".join(temp)
    # print(type(temp), temp)

    uganjena_beseda = ""
    for el in beseda:
        if uganjena_beseda != "":
            uganjena_beseda += " "
        if el in ugibi:
            uganjena_beseda += el
        else:
            uganjena_beseda += "_"
    print(uganjena_beseda)
    print(f"Dosedanji ugibi: {ugibi}")
    print(f"ostalih ugibanj: {st_ugibanj}")

    # 2. Uporabnika vprašamo naj vtipka kero črko ugiba
    crka = input("What is your guess? ").strip()
    if len(crka) != 1:
        print(f"Napačen vnos! Vnos '{crka}' ima več kot en znak! Poskusi znova!")
        continue

    if crka in ugibi:
        print(f"Napačen vnos! Vnos '{crka}' je že bil vnesen! Poskusi znova!")
        continue

    print(f"Ugibalo se je črko: '{crka}'")
    ugibi.append(crka)

    # 3. Preverimo ali je črka del besede
    if crka in beseda:
        print("Črka je del besede")
        word_check[crka] = True
    else:
        print("Črka NI del besede")

    # 4. Preverimo ali je uganil besedo
    # 4.a Če je uganil besedo je zmagal. Konec igre
    # 4.b Če ni uganil cele besede in nima več možnih ugibov je izgubil. Konec igre
    # 4.c Če ni uganil cele besede in ima še ugibe gremo na korak 1.
    if False in word_check.values():
        won = False
    else:
        won = True

    st_ugibanj -= 1
    if won:
        break


if won:
    print("ZAMAGA!")
else:
    print("Poraz.")
