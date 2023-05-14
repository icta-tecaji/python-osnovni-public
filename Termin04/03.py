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
    
#  Naloga:

# Dodajte še kodo, ki od uporabnika zahteva naj vnesejo v katero polje 
#  želijo postaviti svoj znak.


# 1. Prikažemo igralno ploščo
print("R\\C 0 1 2")
for (i, row) in enumerate(board):
    print(f"{i}   {row[0]} {row[1]} {row[2]}")
# 2. Od igralca zahtevamo naj naredi potezo
move = input(f"make a move (R/C) (exp: 12): ")
print(move, type(move), len(move))
row = int(move[0])
column = int(move[1])
print(row,type(row))
board[row][column] = "X"



print("R\\C 0 1 2")
for (i, row) in enumerate(board):
    print(f"{i}   {row[0]} {row[1]} {row[2]}")

# 3. preverimo ali je kdo zmagoval
# 3.a Če je kdo zmagal, izpišemo zmagovalca
# 3.b Če ni zmagovalca gremo na korak 1
