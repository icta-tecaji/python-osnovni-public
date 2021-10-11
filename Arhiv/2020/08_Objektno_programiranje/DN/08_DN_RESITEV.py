'''
Naloga: 
Napišite funkcijo razadalja_v_pomnilniku(prvi_atribut, drugi_atribut), ki vrne koliko narazen so si objekti v pomnilniku.

Razdalje se bodo razlikovale po vsakem novem zagonu.


Primeri:

Input:
    a = 1
    b = [2,3,4]
    c = {"prvi": 8, "drugi": 9, "tretji":10}
    print(f"a <--- {razadalja_v_pomnilniku(a,b)} ---> b")
    print(f"a <--- {razadalja_v_pomnilniku(a,c)} ---> c")
    print(f"b <--- {razadalja_v_pomnilniku(b,c)} ---> c")

Output:
    # razdalje se bodo razlikovale po vsakem zagonu
    a <--- 72999760 ---> b
    a <--- 90437904 ---> c
    b <--- 17438144 ---> c
'''
# Rešitev
def objDiff(a,b):
    return abs(id(a)-id(b))

a = 1
b = [2,3,4]
c = {"prvi": 8, "drugi": 9, "tretji":10}
print(f"a <--- {objDiff(a,b)} ---> b")
print(f"a <--- {objDiff(a,c)} ---> c")
print(f"b <--- {objDiff(b,c)} ---> c")



'''
Naloga: 
Napiši razred Zaposlena_oseba, ki ima v sebi shranjene parametre ime, priimek in placa, ki jih prejme ob inicializaciji. Vsebuje naj tudi funkcijo razlika_v_placi ki kot parameter prejme objekt tipa Zaposlena_oseba ki predstavlja neko drugo osebo. Funkcija naj vrne absolutno razliko med plačama osebe v kateri se funkcija kliče ter pa osebe, ki je bila podana kot parameter.
Ne pozabite na parameter "self". Uporabite ga tam kjer je potrebno. 

Primeri:

Input:
    zaposleni = [Zaposlena_oseba("Luka", "Novak", 1500.0),
                 Zaposlena_oseba("Živa", "Groza", 2100.0),
                 Zaposlena_oseba("Anže", "Jaklin", 1436.50),
                 Zaposlena_oseba("Luka", "Bogataj", 1790.0),
                 Zaposlena_oseba("Sara", "Ljubljen", 3600.0)]

    print("Razlika med plačami zaposlenih:")
    for i in range(len(zaposleni)):
        for j in range(i+1, len(zaposleni)):
            ime1 = zaposleni[i].ime
            priimek1 = zaposleni[i].priimek
            razlika = zaposleni[i].razlika_v_placi(zaposleni[j])
            ime2 = zaposleni[j].ime
            priimek2 = zaposleni[j].priimek
            print(f"\t{ime1} {priimek1} <--- {razlika} € ---> {ime2} {priimek2}")

Output:
    Razlika med plačami zaposlenih:
        Luka Novak <--- 600.0 € ---> Živa Groza
        Luka Novak <--- 63.5 € ---> Anže Jaklin
        Luka Novak <--- 290.0 € ---> Luka Bogataj
        Luka Novak <--- 2100.0 € ---> Sara Ljubljen
        Živa Groza <--- 663.5 € ---> Anže Jaklin
        Živa Groza <--- 310.0 € ---> Luka Bogataj
        Živa Groza <--- 1500.0 € ---> Sara Ljubljen
        Anže Jaklin <--- 353.5 € ---> Luka Bogataj
        Anže Jaklin <--- 2163.5 € ---> Sara Ljubljen
        Luka Bogataj <--- 1810.0 € ---> Sara Ljubljen
'''
# Rešitev
class Zaposlena_oseba:
    def __init__(self, ime, priimek, placa):
        self.ime = ime
        self.priimek = priimek
        self.placa = placa
        
    def razlika_v_placi(self,druga_oseba):
        return abs(self.placa-druga_oseba.placa)

zaposleni = [Zaposlena_oseba("Luka", "Novak", 1500.0),
             Zaposlena_oseba("Živa", "Groza", 2100.0),
             Zaposlena_oseba("Anže", "Jaklin", 1436.50),
             Zaposlena_oseba("Luka", "Bogataj", 1790.0),
             Zaposlena_oseba("Sara", "Ljubljen", 3600.0)]

print("Razlika med plačami zaposlenih:")
for i in range(len(zaposleni)):
    for j in range(i+1, len(zaposleni)):
        ime1 = zaposleni[i].ime
        priimek1 = zaposleni[i].priimek
        razlika = zaposleni[i].razlika_v_placi(zaposleni[j])
        ime2 = zaposleni[j].ime
        priimek2 = zaposleni[j].priimek
        print(f"\t{ime1} {priimek1} <--- {razlika} € ---> {ime2} {priimek2}")

'''
Naloga: 
Napiši razred Krizci_in_krozci, ki simulira izvajanje igre "kržci in krožci".
Funkcije ki jih naj podpira:
    __init__(self), ki inicializira celoten razred, ki se bo lahko uporabljal za igranje

    mark_X(self, row_index, column_index), ki označi X na željeno mesto

    mark_O(self, row_index, column_index), ki označi O na željeno mesto

    check_win(self), ki pregleda ali je kdo zmagal in napiše točno kdo je zmagal

    reset(self), ki pobriše že igrane X in O

    print_current_position(self), ki izriše trenutno pozicijo igre v obliki kvadrata, kjer je vsaka celica označena s trenutnimi znaki (za izgled si poglej "Otput" primera spodaj). 

Primeri:

Input:
    igra = Krizci_in_krozci()
    plays = [(1,1),(0,0),
             (0,2),(1,0),
             (2,0)]

    for i in range(len(plays)):
        if i%2==0:
            igra.mark_X(plays[i][0],plays[i][1])
        else:
            igra.mark_O(plays[i][0],plays[i][1])
        igra.print_current_position()
        igra.check_win()
        print("")
        igra.check_win()
    igra.reset()
    igra.print_current_position()


Output:
    -------------
    |   |   |   |
    -------------
    |   | X |   |
    -------------
    |   |   |   |
    -------------

    -------------
    | O |   |   |
    -------------
    |   | X |   |
    -------------
    |   |   |   |
    -------------

    -------------
    | O |   | X |
    -------------
    |   | X |   |
    -------------
    |   |   |   |
    -------------

    -------------
    | O |   | X |
    -------------
    | O | X |   |
    -------------
    |   |   |   |
    -------------

    -------------
    | O |   | X |
    -------------
    | O | X |   |
    -------------
    | X |   |   |
    -------------

    Igralec, ki je označeval z X-em je zmagovalec!
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
'''
# Rešitev
class Krizci_in_krozci:
    def __init__(self):
        self.mreza = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    
    def mark_X(self, row_index, column_index):
        self.mreza[row_index][column_index] = 'X'
    
    def mark_O(self, row_index, column_index):
        self.mreza[row_index][column_index] = 'O'
    
    def check_win(self):
        win_mark = ""
        if self.mreza[0][0] == self.mreza[1][0] == self.mreza[2][0] != ' ':   # left column
            win_mark = self.mreza[0][0]
        elif self.mreza[0][1] == self.mreza[1][1] == self.mreza[2][1] != ' ': # middle column
            win_mark = self.mreza[0][1]
        elif self.mreza[0][2] == self.mreza[1][2] == self.mreza[2][2] != ' ': # right column
            win_mark = self.mreza[0][2]
        elif self.mreza[0][0] == self.mreza[0][1] == self.mreza[0][2] != ' ': # top row
            win_mark = self.mreza[0][0]
        elif self.mreza[1][0] == self.mreza[1][1] == self.mreza[1][2] != ' ': # middle row
            win_mark = self.mreza[1][0]
        elif self.mreza[2][0] == self.mreza[2][1] == self.mreza[2][2] != ' ': # bottom row
            win_mark = self.mreza[2][0]
        elif self.mreza[0][0] == self.mreza[1][1] == self.mreza[2][2] != ' ': # diagonal left-top to right-bottom
            win_mark = self.mreza[0][0]
        elif self.mreza[0][2] == self.mreza[1][1] == self.mreza[2][0] != ' ': # diagonal left-bottom to right-top
            win_mark = self.mreza[2][0]
        
        if win_mark != "":
            print(f"Igralec, ki je označeval z {win_mark}-em je zmagovalec!")
    
    def reset(self):
        self.mreza = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        
    def print_current_position(self):
        print(f"-------------")
        print(f"| {self.mreza[0][0]} | {self.mreza[0][1]} | {self.mreza[0][2]} |")
        print(f"-------------")
        print(f"| {self.mreza[1][0]} | {self.mreza[1][1]} | {self.mreza[1][2]} |")
        print(f"-------------")
        print(f"| {self.mreza[2][0]} | {self.mreza[2][1]} | {self.mreza[2][2]} |")
        print(f"-------------")


igra = Krizci_in_krozci()
plays = [(1,1),(0,0),
         (0,2),(1,0),
         (2,0)]

for i in range(len(plays)):
    if i%2==0:
        igra.mark_X(plays[i][0],plays[i][1])
    else:
        igra.mark_O(plays[i][0],plays[i][1])
    igra.print_current_position()
    print("")
    igra.check_win()
igra.reset()
