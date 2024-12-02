# Polica

# Ustvarite razred Polica.

#     Vsaka instanca razreda naj ima:
#         knjige -> list naslovov knjig, ki se nahajajo na polici
#         max_knjig -> integer vrednost, ki pove koliko knjig, gre maximalno na polico
#     Ko ustvarimo instanco razreda vanj posredujemo številko maximalnih knjig na polici.
#
#     Ko ustvarimo instanco razreda vanj posredujemo lahko tudi list naslovov knjig, ki se že nahajajo na polici.
#     Če takega seznama ne posredujemo naj ima polica prazen seznam.
#
#     Razred naj ima metodo kaj_je_na_polici, ki naj vrne list naslovov knjig
#     Razred naj ima metodo dodaj_knjigo, ki kot argument prejme string naslova knjige.
#     To knjigo naj doda v list naslovov knjig, če s tem ne presežemo maximalno število knjig.
#     Če bi presegli to število knjige ne dodamo.

#     Razred naj ima metodo uredi_knjige, ki kot argument ascending prejme boolean vrednost, ki nam pove ali naj
#     bodo knjige urejene (glede na prvo črko) v A->Z (vrednost True) oziroma Z->A (vrednost False). Če ta vrednost ni bila posredovana
#     naj bo default vrstni red A->Z. Metoda naj uredi list naslovov knjig in tega nato vrne


class Polica:
    def __init__(self, max_knjig, knjige=None):
        self.max_knjig = max_knjig
        self.knjige = knjige if knjige else []

    def kaj_je_na_polici(self):
        return self.knjige

    def dodaj_knjigo(self, naslov):
        if len(self.knjige) < self.max_knjig:
            self.knjige.append(naslov)
        else:
            print(f"Ne morem dodati '{naslov}'. Polica je polna.")

    def uredi_knjige(self, ascending=True):
        self.knjige.sort(reverse=not ascending)
        return self.knjige


polica = Polica(7, ["The Witcher", "Dune", "Harry Potter", "Hamlet", "Tintin", "SSKJ"])
print(polica.kaj_je_na_polici())

print(polica.uredi_knjige())

polica.dodaj_knjigo("Romeo in Julija")
print(polica.kaj_je_na_polici())

polica.dodaj_knjigo("Game of Thrones")
print(polica.kaj_je_na_polici())

print(polica.uredi_knjige(False))
