board = [
	["E", "E", "E"],
	["E", "E", "E"],
	["E", "E", "E"]
]

def display_board():
	print("R\\C 0 1 2")
	for (i, row) in enumerate(board):
		print(f"{i}   {row[0]} {row[1]} {row[2]}")

def make_move(char):
	print(f"It's {char}'s turn.")
	move = input(f"make a move (R/C) (exp: 12): ")
	row = int(move[0])
	column = int(move[1])
	board[row][column] = char
    
while True:
	# 1. Prikažemo igralno ploščo
	display_board()
	# 2. Od igralca zahtevamo naj naredi potezo
	make_move("O")

	# 3. preverimo ali je kdo zmagoval
		# 3.a Če je kdo zmagal, izpišemo zmagovalca
		# 3.b Če ni zmagovalca gremo na korak 1
	
	# 4. preverimo, če je board že poven
	board_1D = []
	for row in board:
		board_1D.extend(row)
	if not ("E" in board_1D):
		break

#  Naloga:

# Za konec dodajmo to vse v while zanko, ki se izvaja dokler obstaja še kakšna možna poteza.

# Možna poteza obstaja, če obstaja "E" znotraj naše igralne plošče.

# Primeri:


# R\C 0  1  2
# 0   E  E  E
# 1   E  E  E
# 2   E  E  E
# It's O's turn.
# Make a move (R/C) (exp: 12): 12
# R\C 0  1  2
# 0   E  E  E
# 1   E  E  O
# 2   E  E  E
# It's O's turn.
# Make a move (R/C) (exp: 12): 11
# R\C 0  1  2
# 0   E  E  E
# 1   E  O  O
# 2   E  E  E
# It's O's turn.
# Make a move (R/C) (exp: 12): 00
# R\C 0  1  2
# 0   O  E  E
# 1   E  O  O
# 2   E  E  E
# It's O's turn.
# Make a move (R/C) (exp: 12): 02
# R\C 0  1  2
# 0   O  E  O
# 1   E  O  O
# 2   E  E  E
# It's O's turn.
# Make a move (R/C) (exp: 12): 21
# R\C 0  1  2
# 0   O  E  O
# 1   E  O  O
# 2   E  O  E
# It's O's turn.
# Make a move (R/C) (exp: 12): 22
# R\C 0  1  2
# 0   O  E  O
# 1   E  O  O
# 2   E  O  O
# It's O's turn.
# Make a move (R/C) (exp: 12): 01
# R\C 0  1  2
# 0   O  O  O
# 1   E  O  O
# 2   E  O  O
# It's O's turn.
# Make a move (R/C) (exp: 12): 10
# R\C 0  1  2
# 0   O  O  O
# 1   O  O  O
# 2   E  O  O
# It's O's turn.
# Make a move (R/C) (exp: 12): 20

