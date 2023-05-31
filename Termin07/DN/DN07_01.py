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
'''