# Variable scope

def neki2():
	print(a)

a = 123

neki2()

print(a)

def neki():
	b = 7
	print(a)
neki()

# print(b) --> vrne napako
b = 7
print(b)



def fun(spr1):
	spr2 = 10
	print(spr1)
	print(spr2)

print(fun(5))
#print(spr1)
#print(spr2)


a = 10
if a > 20 or True:
	spr5 = 100

print(spr5)

for i in range(10):
	nekaj_novega = i

print(nekaj_novega)


a = 10
def fun(a):
	# local > global
	print(a)

print()
print(a)
print()
fun(5)

print()
print(a)
print()


def fun(s):
	print(s)
	s[0] = 100

seznam = [3,7,13]
fun(seznam)
print(seznam)

print()
seznam = [3,7,13]
fun(seznam.copy())
print(seznam)


temp = {"a":1, "b":19}
def fun(d):
	print(d)
	d["a"] = 2
print()
fun(temp)
print(temp)
print()


spr1 = 5
print(spr1)

def fun():
	global spr1
	spr1 = 100
	print(spr1)

fun()
print(spr1)
print()




# Naloga:
# Napišite funkcijo, kjer lahko igramo vislice.
# Funkcija vislice() naj ima 2 parametra. Prvi je besedo katero se ugiba in drugi število možnih ugibov. Če števila ugibov ne podamo naj bo default vrednost 10.
# Uporabnika konstantno sprašujte naj vnese črko. Nato izpišite iskano besedo. Črke katere je uporabnik uganil izpišite normalno, črke katere še ni uganil pa nadomestite z _.
# Dodatno zraven prikazujte katere vse črke je uporabnik že preizkusil.
# Če uporabnik besedo uspešno ugani v danih poizkusih naj funkcija vrne vrednost True. V nasprotnem primeru naj vrne vrednost False.

# ta funkcija igra vislice
def vislice(beseda,st_moznih_ugibov=10):
	correct_guesses = []
	all_guesses = []
	counter = 0
	while counter < st_moznih_ugibov:
		guess = input(f"Guesses so far: {all_guesses}\nWhat is your guess? ")

		all_guesses.append(guess)
		if guess in beseda:
			correct_guesses.append(guess)
		
		temp = ""
		for char in beseda:
			if char in all_guesses:
				temp += char
			else:
				temp += " _ "

		print(temp)
		#flag_is_done = True
		#for char in beseda:
		#	if char not in correct_guesses:
		#		flag_is_done = False
		#		break
		#if len(set(beseda)) == len(set(correct_guesses)):
		if beseda == temp:
			print("KONEC !!!")
			return True

		# preverimo če je uporabnik ugotovil besedo

		counter += 1
	return False

# test
#x = vislice("jabolko")
#if x==True:
#	print("Uporabnik je uganil besedo!")
#else:
#	print("Uporabnik ni uganil besede!")



# Naloga:
# Ustvarite program Križci in Krožci
# Igralno polje lahko predstavite kot liste znotraj lista, kjer E predstavlja prazno polje.
# board = [["X", "E", "E"],
#          ["O", "E", "E"],
#          ["E", "E", "E"]]
# Od igralcev nato izmenično zahtevajte polje v katerega želijo postaviti svoj znak.
# Privzememo lahko, da bodo igralci igrali pravično in vpisovali samo prazna polja.


board = [["X", "E", "E"],
         ["O", "E", "E"],
         ["E", "E", "E"]]

def display_board(board):
	for row in board:
		print(row)

print(board)
print()
display_board(board)

def whos_turn_it_is(index=0):
	players = ["X","O"]
	while True:
		yield players[index]
		if index == 0:
			index = 1
		elif index == 1:
			index = 0
		#index = (index + 1) % len(players)

def board_full(board):
	for row in board:
		for char in row:
			if char == "E":
				return False
	return True

def make_a_move(player, board):
	#str_in = "1,1"
	#indexes = str_in.split(",") # ["1","1"]
	#row_index = int(indexes[0])
	#column_index = int(indexes[1])
	row_index = int(input(f"In which row (index) do you want to put '{player}'? "))
	column_index = int(input(f"In which column (index) do you want to put '{player}'? "))
	board[row_index][column_index] = player

def who_is_a_winer(board):
	# pogledamo če je kakšna vrstica ki ima vse iste znake IN ti niso "E"
	for row in board:
		# if (row[0] == row[1] and row[1]==row[2]) and (row[0] != "E"):
		if (row[0] == row[1] == row[2]) and (row[0] != "E"):
			return row[0]
	# pogledamo če je kakšen stolpec ki ima vse iste znake IN ti niso "E"
	for i in range(3):
		if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != "E"):
			return board[0][i]
	# pogledamo 1. diagonalo (od levo-zogoraj do desno-spodaj)
	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != "E"):
		return board[0][0]
	# pogledamo 2. diagonalo (od desno-spodaj do levo-zgoraj)
	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != "E"):
		return board[0][2]
	# vrnemo "E" če ni zmagovalca
	return "E"

def play():
	board = [["E", "E", "E"],
			 ["E", "E", "E"],
			 ["E", "E", "E"]]
	who_to_begin = int(input("Who to start (for X type in '0', for O type in '1')? "))
	player_gen = whos_turn_it_is(who_to_begin)
	while True:
		# pazi na to kdo je na vrsti
		player = next(player_gen)
		print(f"Whose turn it is: '{player}'")
		# prikaži trenuten board
		print()
		display_board(board)
		# poteze igre
		print()
		make_a_move(player,board)
		# preveri če je že kdo zmagal
		player_who_won = who_is_a_winer(board)
		# če nekdo zmaga, to povej in zaključi igro
		if player_who_won != "E":
			print("\n\nFinal board:")
			display_board(board)
			print(f"\nWIN: {player_who_won}\n")
			break
		# zaključi če ni več drugih potez
		if board_full(board):
			print("Board je poven, brez zmagovalca!")
			break
	print("Hvala za igro! poskusi še kdaj :)")
		
print()
print()


play()





