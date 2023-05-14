# Križci in krožci

# Primer igranja igre:

# Output:
# ['E', 'E', 'E']
# ['E', 'E', 'E']
# ['E', 'E', 'E']
# It's X's turn. Make a move (exp: 12): '00

# ['X', 'E', 'E']
# ['E', 'E', 'E']
# ['E', 'E', 'E']
# It's O's turn. Make a move (exp: 12): '12

# ['X', 'E', 'E']
# ['E', 'E', 'O']
# ['E', 'E', 'E']
# It's X's turn. Make a move (exp: 12): '10

# ['X', 'E', 'E']
# ['X', 'E', 'O']
# ['E', 'E', 'E']
# It's O's turn. Make a move (exp: 12): '12

# ['X', 'E', 'E']
# ['X', 'E', 'O']
# ['E', 'E', 'E']
# It's X's turn. Make a move (exp: 12): '20
# X je ZMAGOVALEC!

# https://collabedit.com/ss4gf

# Ustvarimo spremenljivko v kateri bomo shranili stanje naše plošče

# 1. Prikažemo igralno ploščo
# 2. Od igralca zahtevamo naj naredi potezo
# 3. preverimo ali je kdo zmagoval
# 3.a Če je kdo zmagal, izpišemo zmagovalca
# 3.b Če ni zmagovalca gremo na korak 1

board = [
    ["E","E","E"],
    ["E","E","E"],
    ["E","E","E"]
]
# board = [a, b, c]
# board[0] --> a
# a = ["E","E","E"]
# board[0][1] = "X"
# print(board)
# print("R\\C")
# print("\n")

# if "\" before "n":
# 	naredi novo vrstivo
# else:
#     izpiši črko n

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

#  Naloga:

# Implementirajte še potezo katero naredi igralec znotraj
# funkcije make_move().

# Primeri:

# R\C 0  1  2
# 0   E  E  E
# 1   E  E  E
# 2   E  E  E
# Make a move (R/C) (exp: 12): 12
# R\C 0  1  2
# 0   E  E  E
# 1   E  E  X
# 2   E  E  E
