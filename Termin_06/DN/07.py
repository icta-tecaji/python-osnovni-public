"""
Naloga:

Napiši razred Pikado, ki ima v sebi shranjene spremenljivke igralci, ki je list števil dolžine "stevilo_igralcev", ki so ob inicializaciji nastavljeni na vrednost "stevilo_zacetnih_tock" (stevilo_igralcev in stevilo_zacetnih_tock sta atributa podana ob klicu funkcije). Instanca razreda naj ima tudi spremenljivko na_potezi, ki predstavlja indeks igralca na potezi (tekom igre, naj se ta spremenljivka spreminja in uporablja za sledenju kateri igralec je na vrsti in kateri je naslenji). Igra bo simulirala igro pikado, kjer je cilj, da igralec zniža svoje točke točno do 0 (če gre v svojem krogu, pod to vrednost, se mu vrednost resetira na vrednost pred njegovim prvim metom). Vsak igralec ima 3 mete na potezo. Meti naj bodo zabeleženi z uporabo funkcije input(...)

Vsebuje naj tudi funkcije:

    "zazeni_igro", ki simulira igro z neskončno zanko in klicanjem metode "vrzi". Ne pozabite preverjati, ali se igra zaključi.
    
    "vrzi", ki simulira vse 3 mete igralca, ki je sedaj na potezi. Vsak met, ki ga igralec naredi, naj se uporabi kot odštevek za njegove točke v spremenljivki instance igralci. Funkcija naj vrne True, če je igralec zmagal in False, če ni.
    
    "preveri_ali_je_konec", ki preverja če je trenutnemu igralcu uspelo priti točno do "0" točk. Če ja, vrnite True, drugače False. Metoda naj ob zmagim tudi izpiše niz "Zmagovalec je x" (x zamenjajte z indeksom igralca, ki je zmagal).

"""