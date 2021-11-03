'''
Napišite razred Kalkulator, ki bo simuliral delovanje kalkulatorja. Kalkulator mora tudi beležiti koliko napak je prišlo pri samem izvajanju. Torej morebitne napake mora kalkulator predvideti in uporabniku povedati pri kateri operaciji je prišlo do napake ter opis same napake (prve ki se pojavi), vendar se kalkulator/program ne sme ustaviti. Kalkulator se lahko zaključi z vnešenim operatorjem "q". Podpira naj vsaj seštevanje "+", odštevanje "-", množenje "*", deljenje "/" in potenciranje "**". Ob koncu izvajanja, mora kalkulator izpisati koliko napak je naredil uporabnik (1 napaka se šteje za napako pri 1 izračunu --> torej če sta x in y narobe vnešena se to šteje samo za 1 napako).

Kaj vse mora nuditi kalkulator:
- pomoč, kateri operatorji so na voljo
- vnos operatorja ("input()")
- vnos števila x ("input()")
- vnos števila y ("input()")
- ob napaki izpiše katero operacija je bila mišljeno izvesti in opis napake ki jo vrne program
- izpis operacije (vsakič), tudi če pride do napakev obliki: "[x] [operator] [y] = rezultat" naprimer: "[3] [**] [3] = 27"
- ob napaki, naj za rezultat izpiše "None", naprimer: "[3] [***] [0] = None"
- vsako izvajanje naj bo ločeno s črto (poglej si primer izvajanja)
    

Input:
    calc = Kalkulator()
    calc.start()

Output:
    Operatorji:
            [+] --> seštevanje
            [-] --> odštevanje
            [*] --> množenje
            [/] --> deljenje
            [**] --> potenciranje
            [q] --> zaključi kalkulator
    Operator: *
    x = 6
    y = 6
    [6] [*] [6] = 36.0
    ---------------------------------------------------------------------------

    Operatorji:
            [+] --> seštevanje
            [-] --> odštevanje
            [*] --> množenje
            [/] --> deljenje
            [**] --> potenciranje
            [q] --> zaključi kalkulator
    Operator: 8*
    x = *
    y = *
    Prišlo je do napake pri <neznana operacija>: Operator je vnešen napačno
    [*] [8*] [*] = None
    ---------------------------------------------------------------------------

    Operatorji:
            [+] --> seštevanje
            [-] --> odštevanje
            [*] --> množenje
            [/] --> deljenje
            [**] --> potenciranje
            [q] --> zaključi kalkulator
    Operator: 
    x = 
    y = 
    Prišlo je do napake pri <neznana operacija>: Operator je vnešen napačno
    [] [] [] = None
    ---------------------------------------------------------------------------

    Operatorji:
            [+] --> seštevanje
            [-] --> odštevanje
            [*] --> množenje
            [/] --> deljenje
            [**] --> potenciranje
            [q] --> zaključi kalkulator
    Operator: /
    x = asffds
    y = 
    Prišlo je do napake pri <deljenje>: could not convert string to float: 'asffds'
    [asffds] [/] [] = None
    ---------------------------------------------------------------------------

    Operatorji:
            [+] --> seštevanje
            [-] --> odštevanje
            [*] --> množenje
            [/] --> deljenje
            [**] --> potenciranje
            [q] --> zaključi kalkulator
    Operator: -
    x = 3.589
    y = 7.98
    [3.589] [-] [7.98] = -4.391
    ---------------------------------------------------------------------------

    Operatorji:
            [+] --> seštevanje
            [-] --> odštevanje
            [*] --> množenje
            [/] --> deljenje
            [**] --> potenciranje
            [q] --> zaključi kalkulator
    Operator: q
    število napak v času delovanja: 3

'''
# Rešitev
class Kalkulator:
    def __init__(self):
        self.numOfMistakes = 0
        
    def start(self):
        while True:
            print("""\nOperatorji:
        [+] --> seštevanje
        [-] --> odštevanje
        [*] --> množenje
        [/] --> deljenje
        [^] --> potenciranje
        [q] --> zaključi kalkulator""")
            operator = input("Operator: ").strip()

            if operator == "q":
                self.izpisi_stevilo_napak()
                break

            x = input("x = ").strip()
            y = input("y = ").strip()

            rezultat = self.izracunaj(operator,x,y)

            print(f"[{x}] [{operator}] [{y}] = {rezultat}")
            print("---------------------------------------------------------------------------")
        
    def izracunaj(self,operator, num1, num2):
        operacije_dict = {"+":"seštevanje",
                         "-":"odštevanje",
                         "*":"množenje",
                         "/":"deljenje",
                         "^":"potenciranje"}
        try:
            if operator in operacije_dict:
                operacija = operacije_dict[operator]
            else:
                operacija = "neznana operacija"
                raise Exception("Operator je vnešen napačno")
            num1_f = float(num1)
            num2_f = float(num2)
            if operator == "+":
                return num1_f+num2_f
            elif operator == "-":
                return num1_f-num2_f
            elif operator == "*":
                return num1_f*num2_f
            elif operator == "/":
                return num1_f/num2_f
            elif operator == "^":
                return num1_f**num2_f
            else:
                raise Exception(f"Operacija ni bila možno zaznati iz opratorja <{operator}>")
        except Exception as e:
            self.numOfMistakes += 1
            print(f"Prišlo je do napake pri <{operacija}>: {e}")
            return None
        
        
    def izpisi_stevilo_napak(self):
        print(f"število napak v času delovanja: {self.numOfMistakes}")

calc = Kalkulator()
calc.start()





'''
Napišite funkcijo "izvedi_ukaze(ime_datoteke)", ki prejme kot atribut ime datoteke, v kateri so v vsaki vrstici napisani ukazi, ki jih mora ta funkcija interpretirati. Ukazi se nanašajo na izrisovanje obrob likov. Primer datoteke je datoteka "test.txt".

Oblika ukaza: "[Lik], [Kam_izpisati], [Velikost]"

Lik:
"trikotnik" --> izriše se naj obroba trikotnika
"kvadrat" --> izriše se naj obroba kvadrata



Kam_izpisati:
"terminal" --> izriše se naj v terminalu
"ime_nove_datoteke" --> odpre se naj datoteko z imenom ime_nove_datoteke in vanj tudi izriše


Velikost:
"stevilo_vrstic" --> koliko vrstic naj uporabi za izris (se upošteva tudi koliko je maksimalno znakov v vrstici --> brez '\n')


Ob začetku preverjanja ukaza, naj v terminal izpiše kakšen je prebrani ukaz (lahko kar v listu, kot je narejeno v primerih), nato pa ga naj izvede. Če pride pri izvajanju do napake, naj program v terminalu napiše, da je prišlo do napake ter opis same napake.

Za pomoč:
"split(znak)" --> razdeli string v list, kjer za razdelitev uporabi "znak" podan v oklepaju
"strip()" --> stringu obrže "prazne znake" kot so presledki, tabulatorji, ... Na čisto desni in levi strani stringa

Razultat izvajanja so tudi ustvarjene datoteke
Za primer datotek imate podani datoteki: "primer_kvadrat.txt" in "primer_trikotnik.txt"



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
# Rešitev
def izvedi_ukaze(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as f:
        print("---------------------- izvajanje ukazov ----------------------")
        for line in f:
            command = [ x.strip() for x in line.strip().split(",")]
            print("\nukaz:",command)
            try:
                if command[0] == "trikotnik":
                    draw_triangle(command[1:])
                elif command[0] == "kvadrat":
                    draw_square(command[1:])
                else:
                    raise Exception(f"Ukaz [{command[0]}] neznan")
            except Exception as e:
                print(f"\tTa ukaz ima napako: {e}")
        print("---------------------- ukazi izvedeni ----------------------")

def draw_triangle(args):
    h = int(args[1])
    if args[0] == "terminal":
        for i in range(h):
            if i == h-1:
                print("*"*(i+1))
            else:
                print("*"+" "*max(0,(i-1))+("" if i==0 else "*"))
    else:
        with open(args[0], "w", encoding="utf-8") as f:
            for i in range(h):
                if i == h-1:
                    f.write("*"*(i+1)+"\n")
                else:
                    f.write("*"+" "*max(0,(i-1))+("\n" if i==0 else "*\n"))

def draw_square(args):
    size = int(args[1])
    if args[0] == "terminal":
        for i in range(size):
            if i==0 or i==size-1:
                print("*"*size)
            else:
                print("*"+" "*(size-2)+"*")
    else:
        with open(args[0], "w", encoding="utf-8") as f:
            for i in range(size):
                if i==0 or i==size-1:
                    f.write("*"*size+"\n")
                else:
                    f.write("*"+" "*(size-2)+"*\n")

                    
izvedi_ukaze("test.txt")

