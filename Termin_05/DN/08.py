"""
Naloga:

Napiši razred Artikel, ki ima v sebi shranjene spremenljivke ime, kolicina in cena. Vsi podatki so podani ob inicializaciji.
Napiši razred Nakup, ki ima v sebi sebi spremenljivko nakupi, ki je ob inicializaciji nastavljena na prazni list. Vanj bomo shranjevali artikle. Z razredom "Artikel" bomo ustvarjali artikle ki jih bomo kupili in njihove specifikacije. Z razredom "Nakup" pa bomo sledili vsem kupljenim artiklom. Pazili bomo, da če želimo dodati nov artikel v seznam in je v njem že artikel z enakim imenom in isto ceno, bomo samo povečali količino temu artiklu v seznamu in ne dodali novo inicializiran artikel.

Razred Nakup naj vsebuje tudi funkcije:

    "kupi", ki kot parameter prejme "ime_artikla", "cena_artikla" in "kolicina_artikla" kot atributi ob klicu funkcije. Znotraj te metode, ustvarimo in dodamo nov artikel v list instance nakupi, razen če že obstaja tak artikel v listu, ki ima isto ime in je njegova cena ista. Takrat samo povečamo njegovo količino za "kolicina_artikla", ki smo ga dobili kot atribut ob klicu funkcije.
    
    "za_placilo", ki naj vrne koliko je za plačilo vseh artiklov skupaj (torej za vsak artikel izračunamo ceno z enačbo "količina*cena").
    
    "koliko_naj_mi_vrnejo", ki vrne koliko naj mi blagajničarka vrne, če plačam z vsoto denarja "denar" ki ga dobimo kot atribut ob klicu funkcije (lahko predvidevate, da je "denar" atribut vedno večji od skupne vsote nakupa).
    
    "katere_stvari_imam_najvec", ki vrne ime artikla, katerega imam največ. Če sta 2 artikla z isto količino, naj vrne tistega ki se nahaja bolj na začetku lista nakupi.

"""