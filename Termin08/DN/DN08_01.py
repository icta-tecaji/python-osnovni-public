'''
Naloga: 
Napišite funkcijo izvedi_ukaze(ime_datoteke), ki prejme kot atribut ime datoteke, v kateri so v vsaki vrstici napisani ukazi, ki jih mora ta funkcija interpretirati. Ukazi se nanašajo na izrisovanje obrob likov.


Oblika ukaza: [Lik], [Kam_izpisati], [Velikost]


Lik:
trikotnik --> izriše se naj obroba trikotnika
kvadrat --> izriše se naj obroba kvadrata


Kam_izpisati:
terminal --> izriše se naj v terminalu
ime_nove_datoteke --> odpre se naj datoteko z imenom ime_nove_datoteke in vanj tudi izriše


Velikost:
stevilo_vrstic --> koliko vrstic naj uporabi za izris (se upošteva tudi koliko je maksimalno znakov v vrstici --> brez '\n')


Ob začetku preverjanja ukaza, naj v terminal izpiše kakšen je prebrani ukaz (lahko kar v listu, kot je narejeno v primerih), nato pa ga naj izvede. Če pride pri izvajanju do napake, naj program v terminalu napiše, da je prišlo do napake ter opis same napake.


Za pomoč:
split(znak) --> razdeli string v list, kjer za razdelitev uporabi znak podan v oklepaju
strip() --> stringu obrže "prazne znake" kot so presledki, tabulatorji, ... Na čisto desni in levi strani stringa


Razultat izvajanja so tudi ustvarjene datoteke
Za primer datotek imate podani datoteki: primer_kvadrat.txt in primer_trikotnik.txt

Primeri:

Input:
    izvedi_ukaze("test.txt")

Output (terminal):
    ---------------------- izvajanje ukazov ----------------------

    ukaz: ['kvadrat', 'terminal', '10']
    **********
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    *        *
    **********

    ukaz: ['kvadrat', 'kvadrat_datoteka.txt', '30']

    ukaz: ['trikotnik', 'terminal', 'asd']
        Ta ukaz ima napako: invalid literal for int() with base 10: 'asd'

    ukaz: ['trikotnik', 'terminal', '1']
    *

    ukaz: ['črtica', 'terminal', '80']
        Ta ukaz ima napako: Ukaz [črtica] neznan

    ukaz: ['trikotniknik', 'tr.txt', '-6']
        Ta ukaz ima napako: Ukaz [trikotniknik] neznan

    ukaz: ['trikotnik', 'terminal', '2']
    *
    **

    ukaz: ['trikotnik', 'trikotnik_datoteka.txt', '20']

    ukaz: ['trikotnik', 'terminal', '3']
    *
    **
    ***

    ukaz: ['trikotnik', 'terminal', '4']
    *
    **
    * *
    ****
    ---------------------- ukazi izvedeni ----------------------


Output (datoteke):
    #Preveri podane datoteke
'''