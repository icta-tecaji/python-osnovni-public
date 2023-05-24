board = [
	["E", "E", "E"],
	["E", "E", "E"],
	["E", "E", "E"]
]

def display_board():
	print("R\\C 0 1 2")
	for (i, row) in enumerate(board):
		print(f"{i}   {row[0]} {row[1]} {row[2]}")

def make_move():
	move = input(f"make a move (R/C) (exp: 12): ")
	row = int(move[0])
	column = int(move[1])
	board[row][column] = "X"
    

# 1. Prikažemo igralno ploščo
display_board()
# 2. Od igralca zahtevamo naj naredi potezo
make_move()

# 2.a samo za naše zahteve, izpišimo še enkrat board
display_board()

make_move()
display_board()
make_move()
display_board()

# 3. preverimo ali je kdo zmagoval
	# 3.a Če je kdo zmagal, izpišemo zmagovalca
	# 3.b Če ni zmagovalca gremo na korak 1

