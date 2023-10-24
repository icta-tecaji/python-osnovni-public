#ustvarimo spremenljivko in vanjo zapisemo iskano besedo       
beseda = "lokomotiva"

maxSteviloUgibov = 10

ugibi = []

jeZmagal = False

word_check = {}
for crka in beseda:
    word_check[crka] = False

for i in range(0, maxSteviloUgibov):
    #1. izpisemo ze uganjene crke in stevilo mest _ _ _ _ _ _ _
    izpis = ""
    for crka in beseda:
        if crka in ugibi:
            izpis += crka
        else:
            izpis += "_ "
        
    print(izpis)
    print("Dosedanji ugibi so: " + str(ugibi))
    #2. uporabnika prosimo naj nam vnese crko
    ugib = input("Vnesi crko: ")
    print("uporabnik je vnesel crko: " + ugib)

    ugibi.append(ugib)

    #3. preverimo ali je crka v besedi
    if ugib in beseda:
        print("pravilna crka")
        word_check[ugib] = True
    else:
        print("napacna crka")

    #4. preverimo ali je uganil besedo
    if False in word_check.values():
        jeZmagal = False
    else:
        jeZmagal = True
        break
        

    #4.a ce je uganil mu cestitamo
    #4.b ce ni uganil in mu je zmanjkalo poskusov mu izpisemo da je izgubil
    #4.c ce ni uganil crke ampak so mu se ostali poizkusi, lahko nadaljuje z ugibanjem


if jeZmagal:
    print("Beseda je bila: " + beseda)
    print("Cestitke, zmagal si!")
else:
    print("Zal si izgubil, poskusi znova!")