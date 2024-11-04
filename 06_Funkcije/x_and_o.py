# Ustvarimo spremenljivko v kateri bomo hranili stanje naše plošče
board = [
	["E","E","E"],
	["E","E","E"],
	["E","E","E"],
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
	move = input("Make a move (R/C) (exp: 12): ") # string
	# print(move, type(move))
	row = int(move[0])
	column = int(move[1])
	# print(row, column, type(row), type(column))
	board[row][column] = znak





# NALOGA
# Za konec dodajmo to vse v `while` zanko, ki se izvaja dokler obstaja še kakšna možna poteza.
# Možna poteza obstaja, če obstaja `"E"` znotraj naše igralne plošče.






while True:
	# 1.Prikažemo igralno ploščo "X" in "O"
	display_board()

	# Si zapomniti zaporedje, izmenjajoče


	# 2. Od igralca zahtevamo naj naredi svojo potezo
	make_move("O")

	# 3. Preverit če kdo zmaga oz. če so veljavne poteze

	# 3.a Če je kdo zmagal, izpišemo zmagovalca in zaključimo zanko

	# 3.b Če ni zmagovalca gremo na korak 1

	
	
	# 4 Preverimo če je možna še kakšna poteza, drugače zaključimo zanko
	
	# counter = 0
	# for i in range(3):
	# 	for j in range(3):
	# 		if board[i][j]=="E":
	# 			counter += 1
	# if counter==0: # ni nobenega "E" torej zaključimo igranje 
	# 	print("Ni več možnih potez. Konec igre.")
	# 	break
	
	board_1D = []
	for row in board:
		board_1D.extend(row)
	if not ("E" in board_1D):
		print("Ni več možnih potez. Konec igre.")
		break






# Da lažje debuggiramo bomo dodal še tale prikaz plošče spet
display_board()



