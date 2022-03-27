"""
Naloga:

Napiši razrede DolgaMajica, Pulover, Bunda, SpodnjePerilo, KratkaMajica, DolgeHlace, SpodnjaMajica, KratkeHlace, in Nogavice. Uporabili jih bomo samo za namen ustvarjenja objektov in razločevanje med njimi, torej lahko vsakemu samo napišemo "pass" in smo zaključili z njihovo definicijo (ni potrebno pisatih nobenih metod, niti __init__).

-------------

Napiši razred MojaPotovalkaOblacil, ki ima v sebi parameter obleke, ki je predstavljen kot seznam. Ob inicializaciji instance je ta seznam prazen. V ta seznam bomo dodajali obleke ki so tipa navedenih v zgornjem odstavku. Te podatke bomo uporabili, da bomo ugotovili, če imamo obleke za neko določeno vreme.

Razred MojaPotovalkaOblacil naj vsebuje tudi funkcije:

    "dodaj_obleko", ki kot parameter prejme že ustvarjen objekt tipa enega izmed prvega odstavka in ga naj doda v seznam obleke te instance. Metoda naj ne vrne ničesar.
    
    "ali_imam_obleke_za_vroce_vreme", ki naj vrne True, če se lahko v celotni oblečem za vroče vreme (torej mora biti prisotna vsaj ena instanca od vsakega od teh razredov: KratkaMajica, KratkeHlače), drugače naj vrne False.
    
    "ali_imam_obleke_za_mrzlo_vreme", ki naj vrne True, če se lahko v celotni oblečem za mrzlo vreme (torej mora biti prisotna vsaj ena instanca od vsakega od teh razredov: DolgaMajica, DolgeHlače, Nogavice, Bunda), drugače naj vrne False.


Namig: Za preverjanje, če je nek objekt določenega tipa, lahko uporabite python funkcijo isinstance(... , ...). Podrobno definicijo, dokumentacijo in način uporabe najdete na spletu. 

"""