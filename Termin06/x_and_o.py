board = [["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"]]


def display_board():
    print("R\\C 0 1 2")
    for i, row in enumerate(board):
        print(f"{i}   {row[0]} {row[1]} {row[2]}")


def make_move(znak):
    move = input(f"make a move (R/C) (exp: 12): ")
    row = int(move[0])
    column = int(move[1])
    board[row][column] = znak


def are_moves_left():
    board_1D = []
    for row in board:
        board_1D.extend(row)
    if not ("E" in board_1D):
        return False
    return True


def is_game_over():
    for row in board:
        if row[0] != "E":
            if row[0] == row[1] and row[1] == row[2]:
                return row[0]

    for i in range(3):
        if board[0][i] != "E":
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return board[0][i]

    if board[0][0] != "E":
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]

    if board[0][2] != "E":
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return board[0][2]

    return False


znak = "X"  # začetni igralec

while True:
    # 1. Prikažemo igralno ploščo
    display_board()
    # 2. Od igralca zahtevamo naj naredi potezo
    make_move(znak)
    znak = "X" if znak == "O" else "O"

    # 3. preverimo ali je kdo zmagoval
    # 3.a Če je kdo zmagal, izpišemo zmagovalca
    # 3.b Če ni zmagovalca gremo na korak 1
    winner = is_game_over()
    if winner:
        print("Konec igre:")
        display_board()
        print(f"ZMAGOVALEC: {winner}")
        break

    if not are_moves_left():
        display_board()
        print("NEODLOČENO")
        break
