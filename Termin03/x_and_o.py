#1. Prikaz igralne plošče
board = [["E" , "E" , "E"], 
         ["E" , "E" , "E"], 
         ["E" , "E" , "E"]]

def izris_plosce():
    print("S/V   0    1    2")
    for i,row in enumerate(board):
        print(f"{i}     {row[0]}    {row[1]}    {row[2]}")


def poteza(znak="X"):
    print(f"Igralec {znak} je na potezi.")
    move = input(f" Naredi potezo (S/V) npr. 12: ")
    row =int(move[0])
    col =int(move[1])
    board[row][col] = znak

def poteze_na_voljo():
    board1D=[]
    for row in board:
        board1D.extend(row) #extend() metoda razširi seznam tako, da doda vse elemente podanega seznama (ali kakršnekoli iterable) na konec seznama.
    if not "E" in board1D:
        print("Igra je končana")
        return False
    return True
poteze_na_voljo()==True
znak="X"

def konec_igre():
    for row in board: #Preverba po stolpcih
        if row[0] != "E":
            if row[0] == row[1] and row [0] == row[2]:
                return row[0]
    for i in range(3): #Preverba po vrsticah
        if board[0][i] != "E":
            if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                return board[0][i]
    if board[0][2] != "E":
        if board[0][2]==board[1][1] and board[0][2]==board[2][0]:
            return board[0][2]
    if board [0][0] != "E":
        if board[0][0]==board[1][1] and board[0][0]==board[2][2]:
            return board[0][0]
        
while True:
#while poteze_na_voljo()==True: Druga možnost iteriranja/izvajanja funkcij do zaključka igre

    izris_plosce()
    
    #2. Igralec, ki je na vrsti izbere polje
    poteza(znak)
    znak = "X" if znak == "O" else "O"

    #3. Preverimo, če je kdo zmagal
    poteze_na_voljo()


    
    #3.a Izpišemo zmagovalca
    zmagovalec = konec_igre()
    if zmagovalec:
        print(f"Zmagal je {zmagovalec}")
        izris_plosce()
        break

    #3.b Gremo na korak 1.

    if not poteze_na_voljo():
        izris_plosce()
        print("NEODLOČENO")
        break