# shema izgleda boarda 2D list
board = [
    ["E", "E", "E"],
    ["E", "E", "E"],
    ["E", "E", "E"]
]

# definicija prikaže board
def display_board():
    print()
    print("R\\C 0 1 2")
    for (i, row) in enumerate(board):
        print(f"{i}   {row[0]} {row[1]} {row[2]}")

# definicija premika
def make_move(char):
    print(f"It's {char}'s turn.")
    move = input(f"make a move (R/C) (exp: 12): ")
    row = int(move[0])
    column = int(move[1])
    if board[row][column] == "E":
        board[row][column] = char
    else:
        print()
        print("ILLEGAL MOVE !!!")
        make_move(char)

# definicija preverjanja zmagovalca
def zmagovalec(char):
    # end = False
    # preverjanje zmagovalca v vrstici
    for vrstica in board:
        if vrstica[0] == char and vrstica[1] == char and vrstica[2] == char:
            return True
        else:
            break

    # preverjanje zmagovalca v stolpcu
    for vrstica in range(0, len(board), 1):
        for stolpec in range(0, len(board[vrstica]), 1):
            if board [0][stolpec] == char and board [1][stolpec] == char and board [2][stolpec] == char:
                return True
            else:
                break

    # preverjanje zmagovalca po diagonali
    if (board [0][0] == char and board [1][1] == char and board [2][2] == char) 
        or 
        (board [2][0] == char and board [1][1] == char and board [0][2] == char):
        return True
    else:
        pass

## prikažemo igralno ploščo
display_board()

## izvedemo prvo potezo
poteza = 1

## preverjamo zapolnitev praznih polj, izvajamo poteze izmenično X & O, preverjamo zmagovalca
while poteza < 10:

    ## izmenično določa igralca
    if poteza % 2 == 0:
        char = "X"
    else:
        char = "O"
    print()
    print(poteza, ". poteza", sep="")
    make_move(char)
    poteza += 1
    display_board()

    ## preverja, če obstaja zmagovalec
    zmagovalec(char)
    if zmagovalec (char):
        print()
        print(f"GAME OVER, {char} WON")
        break
    else:
        continue
else:
    print("GAME OVER")


