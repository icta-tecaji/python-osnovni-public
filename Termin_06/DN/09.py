"""
Naloga:

Napiši razred Programer, ki ima v sebi shranjene parametre ime, priimek in programski_jeziki. programski_jeziki naj bo predstavljen kot list vrednosti, vendar je ob inicializaciji nastavljen kot prazen list. Ob klicanju razreda "Programer", sta ob inicializaciji prisotna samo podatka imena in priimka.

Razred Programer naj vsebuje tudi funkcije:

    "dodaj_programski_jezik", ki kot parameter prejme "jezik" (string), ki ga dodamo v list instance programski_jeziki, samo v primeru če ta že ni notri. Metoda naj ne vrne ničesar.
    
    "preveri_ali_programer_ze_zna_programerski_jezik", ki kot parameter prejme "jezik" (string), ki vrne True, če ta programer že zna podani jezik.

-------------

Napiši razred Delavci, ki ima v sebi shranjene parametre programerji, ki naj bo predstavljen kot list vrednosti objektov razreda "Programer", vendar je ob inicializaciji nastavljen kot prazen list. Z razredom "Delavci" bomo hranili seznam delavcev in gledali katere kompetence imamo v svoji ekipi delavcev.

Razred Delavci naj vsebuje tudi funkcije:

    "dodaj_programerja", ki kot parameter prejme že ustvarjen objekt tipa Programer in ga doda v svoj list programerjev.
    
    "zna_kdo_ta_jezik", ki kot parameter prejme "jezik" (string) in preveri, če kateri od programerjev zna programirati s tem jezikom (uporabite že implementirano metodo "preveri_ali_programer_ze_zna_programerski_jezik" razreda "Programer".
    
    "katere_jezike_znajo_delavci_skupaj", ki naj vrne list (seznam) vseh jezikov, ki jih znajo delavci. Vrstni red ni pomemben, pazite le na to, da se jeziki v seznamu ne ponavljajo.

"""