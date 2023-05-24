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
    

# 1. Prikažemo igralno ploščo
display_board()
# 2. Od igralca zahtevamo naj naredi potezo
make_move("O")

	# 2.a samo za naše zahteve, izpišimo še enkrat board
display_board()

# 3. preverimo ali je kdo zmagoval
	# 3.a Če je kdo zmagal, izpišemo zmagovalca
	# 3.b Če ni zmagovalca gremo na korak 1



# Naloga:

# make_move() funkciji dodajte parameter znak, ki drži znak igralca.

# Zaenkrat, ko kličemo funkcijo, hard-codeajmo znak.

# Primeri:

# display_board()
# make_move("O")
# display_board()

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

