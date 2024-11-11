# Ustvarimo spremenljivko v kateri bomo hranili stanje naše plošče
board = [
    ["E", "E", "E"],
    ["E", "E", "E"],
    ["E", "E", "E"],
]


# "display_board"
def display_board():
    print()
    print("R\\C 0 1 2")
    counter = 0
    for row in board:
        # print(row, type(row))
        print(f"{counter}   {row[0]} {row[1]} {row[2]}")
        counter += 1

    # ENUMERATE
    # for (counter,row) in enumerate(board):
    # 	# print(row, type(row))
    # 	print(f"{counter}   {row[0]} {row[1]} {row[2]}")


# "make_move"
def make_move(znak):
    move = input("Make a move (R/C) (exp: 12): ")  # string
    # print(move, type(move))
    row = int(move[0])
    column = int(move[1])
    # print(row, column, type(row), type(column))
    board[row][column] = znak


def are_moves_left():
    # vrne True v primeru če so še možne poteze
    # vrne False če ni več možnih potez
    board_1D = []
    for row in board:
        board_1D.extend(row)
    if "E" not in board_1D:
        print("Ni več možnih potez. Konec igre.")
        return False
    return True

    # counter = 0
    # for i in range(3):
    # 	for j in range(3):
    # 		if board[i][j]=="E":
    # 			counter += 1
    # if counter==0: # ni nobenega "E" torej zaključimo igranje
    # 	print("Ni več možnih potez. Konec igre.")
    # 	break


def is_game_over():
    # preveri vse stolpce in vrstice
    for i in range(3):
        # preverimo vrstice
        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) and (board[i][0] != "E"):
            # "i"-ta vrstica so vsi isti
            # niso "E"-ji
            who_won = board[i][0]
            return who_won
        # preverimo stolpce
        if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]) and (board[0][i] != "E"):
            # "i"-ti stolpec so vsi isti
            # niso "E"-ji
            who_won = board[2][i]
            return who_won
    # preverimo diagonalo \
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] != "E"):
        # diagonala "\" so vsi isti
        # niso "E"-ji
        who_won = board[1][1]
        return who_won
    # preverimo diagonalo /
    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[1][1] != "E"):
        # diagonala "/" so vsi isti
        # niso "E"-ji
        who_won = board[1][1]
        return who_won
    return None  # če ni še zmagovalca, vrnemo "None"


counter = 0

# current_player = "X"

while True:
    # 1.Prikažemo igralno ploščo "X" in "O"
    display_board()

    # Si zapomniti zaporedje, izmenjajoče
    if counter % 2 == 0:  # sodo število
        current_player = "X"
        # make_move("X")
    else:
        current_player = "O"
        # make_move("O")
    counter += 1

    # 2. Od igralca zahtevamo naj naredi svojo potezo
    make_move(current_player)

    # 3. Preverit če kdo zmaga oz. če so veljavne poteze
    winner = is_game_over()
    if winner:
        print("Konec igre:")
        display_board()
        # 3.a Če je kdo zmagal, izpišemo zmagovalca in zaključimo zanko
        print(f"ZMAGOVALEC: {winner}")
        break

    # 3.b Če ni zmagovalca gremo na korak 1 oz. ponovim zanko

    # 4 Preverimo če je možna še kakšna poteza, drugače zaključimo zanko
    if not are_moves_left():
        print("NEODLOČENO")
        break


# Da lažje debuggiramo bomo dodal še tale prikaz plošče spet
# display_board()
