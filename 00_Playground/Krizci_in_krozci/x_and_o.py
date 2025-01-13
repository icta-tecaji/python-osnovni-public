# križci in krožci

#       _____________
#       | - | - | - |
#       _____________
#       | - | - | - |
#       _____________
#       | - | - | - |
#       _____________


# Ustvari spremenljivko v kateri bomo hranili stanje naše plošče
board = [
    ["E", "E", "E"],  # board[row][col]
    ["E", "E", "E"],  # board[row][col]
    ["E", "E", "E"],  # board[row][col]
]


def display_board():
    print()
    print("R\\C 0 1 2")
    for i, row in enumerate(board):
        print(f"{i}   {row[0]} {row[1]} {row[2]}")
    print()


def make_move(znak):
    while True:
        print(f"It's {znak}s turn!")
        move = input("Make a move (R/C) (exp: 12): ")
        row = int(move[0])
        col = int(move[1])
        if board[row][col] == "E":
            board[row][col] = znak
            break
        print(f"Location [row:{row}][col:{col}] is not valid! Try again!")


def switch_player(znak):
    if znak == "X":
        return "O"
    return "X"


def are_moves_left():
    board_1D = []
    for row in board:
        board_1D.extend(row)
    if "E" not in board_1D:
        return False
    return True


def who_won():
    who_is_the_winner = None
    # preveri vrstice (-)
    for row in board:
        if (row[0] == row[1] == row[2]) and (row[0] != "E"):
            who_is_the_winner = row[0]

    # preveri stolpce (|)
    for col_index in range(len(board)):
        if (board[0][col_index] == board[1][col_index] == board[2][col_index]) and (board[0][col_index] != "E"):
            who_is_the_winner = board[0][col_index]

    # preveri eno diagonalo (\)
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != "E"):
        who_is_the_winner = board[0][0]

    # preveri drugo diagonalo (/)
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != "E"):
        who_is_the_winner = board[0][2]

    return who_is_the_winner


current_player = "O"
counter = 0
while True:
    # 0. zamenjamo igralca
    # current_player = "X" if current_player == "O" else "O"
    current_player = switch_player(znak=current_player)

    # 1. Prikažemo igralno ploščo
    display_board()

    # 2. Od igralca zahtevamo naj naredi potezo
    make_move(current_player)

    # 3. Preverimo če kdo zmagal
    winner = who_won()

    # 3.a Če je kdo zmagal, izpišemo zmagovalca
    if winner is not None:
        print(f"Zmagal je {winner}")
        break

    # 3.b Če ni zmagovalca, gremo na korak 1

    # 4. Če ni več možnih potez, ni zmagovalca
    if not are_moves_left():
        print("No more moves are possible!")
        break
