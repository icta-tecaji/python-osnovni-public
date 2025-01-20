# Ustvarite razred `Polica`.
# * Vsaka instanca razreda naj ima:
# * * **knjige** -> list naslovov knjig, ki se nahajajo na polici
# * * **max_knjig** -> integer vrednost, ki pove koliko knjig, gre maximalno na polico
# * Ko ustvarimo instanco razreda vanj posredujemo številko maximalnih knjig na polici.
# * Ko ustvarimo instanco razreda vanj posredujemo lahko tudi list naslovov knjig, ki se
#   že nahajajo na polici. Če takega seznama ne posredujemo naj ima polica prazen seznam.
# * Razred naj ima metodo `kaj_je_na_polici`, ki naj vrne list naslovov knjig
# * Razred naj ima metodo `dodaj_knjigo`, ki kot argument prejme string naslova knjige.
#   To knjigo naj doda v list naslovov knjig, če s tem ne presežemo maximalno število knjig.
#   Če bi presegli to število knjige ne dodamo.
# * Razred naj ima metodo `uredi_knjige`, ki kot argument **ascending** prejme boolean vrednost,
#   ki nam pove ali naj bodo knjige urejene (glede na prvo črko) v A->Z (vrednost True) oziroma Z->A (vrednost False).
#   Če ta vrednost ni bila posredovana naj bo default vrstni red A->Z. Metoda naj uredi list naslovov knjig in tega nato vrne


class Polica:
    def __init__(self, max_knjig, knjige=None):
        if knjige is None:
            self.knjige = []  # list naslovov
        else:
            self.knjige = knjige  # list naslovov
        self.max_knjig = max_knjig  # int koliko knjig je max na polici

    def kaj_je_na_polici(self):
        return self.knjige

    def dodaj_knjigo(self, nova_knjiga):
        if len(self.knjige) < self.max_knjig:
            self.knjige.append(nova_knjiga)

    def uredi_knjige(self, ascending=True):
        # ascending:TRUE --> urejeno na prvo črko A->Z
        # ascending:FALSE --> urejeno na prvo črko Z->A
        self.knjige = sorted(self.knjige, reverse=not ascending)
        return self.knjige


print()
print()
# les = Polica(10, ["The Witcher", "Dune", "Harry Potter", "Hamlet", "Tintin", "SSKJ"])
# print(les.max_knjig, les.knjige)

polica = Polica(7, ["The Witcher", "Dune", "Harry Potter", "Hamlet", "Tintin", "SSKJ"])
print(polica.kaj_je_na_polici())
print(polica.uredi_knjige())

polica.dodaj_knjigo("Romeo in Julija")
print(polica.kaj_je_na_polici())

polica.dodaj_knjigo("Game of Thrones")
print(polica.kaj_je_na_polici())
print(polica.uredi_knjige(False))


polica = Polica(7, ["The Witcher", "Dune", "Harry Potter", "Hamlet", "Tintin", "SSKJ"])
print(polica.kaj_je_na_polici())
# ["The Witcher", "Dune", "Harry Potter", "Hamlet", "Tintin", "SSKJ"]


# print(polica.uredi_knjige())
# ==> ['Dune', 'Hamlet', 'Harry Potter', 'SSKJ', 'The Witcher', 'Tintin']


# polica.dodaj_knjigo("Romeo in Julija")
# print(polica.kaj_je_na_polici())
# ==> ['Dune', 'Hamlet', 'Harry Potter', 'SSKJ', 'The Witcher', 'Tintin', 'Romeo in Julija']


# polica.dodaj_knjigo("Game of Thrones")
# print(polica.kaj_je_na_polici())
# ==> ['Dune', 'Hamlet', 'Harry Potter', 'SSKJ', 'The Witcher', 'Tintin', 'Romeo in Julija']


# print(polica.uredi_knjige(False))
# ==> ['Tintin', 'The Witcher', 'SSKJ', 'Romeo in Julija', 'Harry Potter', 'Hamlet', 'Dune']

print()
print()

# BANKA naloga

# Napišite program:

# ```python
# class Oseba():
#     def __init__(self, ime, priimek):
#         # za to instanco naj ustvari spremenljivki ime in priimek

#     def opis(self):
#         # vrne naj string, znotraj katerega imamo ime in priimek


# class Stranka(): # class naj deduje od razreda Oseba()
#     def nastavi_stanje(self, stanje):
#         # metoda naj ustvari spremenljivko samo za to instaco razreda. Vrednost naj bo "stanje" oziroma default vrednost naj bo 0.
#           Metoda naj nato vrne vrednost spremenljivke stanje

#     def dvig(self, znesek):
#         # Od stanja naj se odšteje znesek.
#         # V kolikor ni dovolj denarja na računu naj se dvigne z banke celotno stanje
#         # Na koncu naj metoda vrne dvignjen znesek

#     def polog(self, znesek):
#         # metoda naj doda velikost zneska stanju
#         # nato naj metoda vrne novo stanje


class Oseba:
    def __init__(self, ime, priimek):
        self.ime = ime
        self.priimek = priimek

    def opis(self):
        return f"Vpisani ste kot stranka: {self.ime} {self.priimek} "


class Stranka(Oseba):
    def nastavi_stanje(self, stanje=0):
        self.stanje = stanje
        return self.stanje

    def dvig(self, znesek):
        hipoteticno_stanje = self.stanje - znesek
        if hipoteticno_stanje < 0:
            print(f"Ni dovolj denarja! Dvignete lahko samo {self.stanje}")
            znesek = self.stanje
            self.stanje = 0
            return znesek
        self.stanje = hipoteticno_stanje
        return znesek

    def polog(self, znesek):
        # znesek = self.stanje + znesek
        self.stanje = self.stanje + znesek
        return self.stanje


# INPUT:
objekt = Stranka("Gregor", "Balkovec")
print(objekt.opis())
print(objekt.nastavi_stanje())
print(objekt.polog(5000))
print(objekt.dvig(2000))
print(objekt.dvig(4000))

# OUTPUT:
# Gregor Balkovec
# 0.0
# 5000.0
# 2000
# Dal ti bom samo 3000.0
# 3000.0
# ```
