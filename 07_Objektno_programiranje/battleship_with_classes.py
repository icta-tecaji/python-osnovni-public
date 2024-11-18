# R/C 0  1  2  3  4  5  6  7  8  9
# 0   .  .  .  .  .  .  .  .  .  .
# 1   .  .  .  .  .  .  .  .  .  .
# 2   .  .  .  .  .  .  .  .  .  .
# 3   .  .  .  .  .  .  .  .  .  .
# 4   .  .  S  '  .  .  .  .  .  .
# 5   .  .  .  .  .  .  .  .  .  .
# 6   .  .  .  .  .  .  .  .  .  .
# 7   .  .    .  .  .  .  .  .  .
# 8   .  .  .  .  .  .  .  .  .  .
# 9   .  .  .  .  .  .  .  .  .  .

# ~ - voda
#  - ladja (ship)
# H - zadetek (hit)
# M - mimo (miss)
# ```


# ======================================================================================
# ======================================================================================
# ======================================================================================

# NALOGA

# Dopolnimo naš program tako, da mu dodamo class `Ship`. Instanca razreda naj ima sledeče atribute:

# name - ime ladje
# length - dolžina ladje
# row , col - začetne koordinate ladje
# orientation - ali je ladja obrnjena horizontalno ali vertikalno
# place_ship - metoda, s katero nastavimo row, col, orientation ladje


class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.row = None
        self.col = None
        self.orientation = None

    def place_ship(self):
        print(f"Placing ship {self.name} ({self.length})")

        self.row = int(input("Vnesi vrstico: "))
        self.col = int(input("Vnesi stolpec: "))
        self.orientation = input("Vnesi orientacijo (V/H): ")


# ======================================================================================
# ======================================================================================
# ======================================================================================
# ======================================================================================
# ======================================================================================
# ======================================================================================
# ======================================================================================

# grid = create_grid()

# display_grid(grid, [])
# player1_ships = [
#     {"name": "Patrol Boat", "length": 2, "row": None, "col": None, "orientation": None},
#     {"name": "Submarine", "length": 3, "row": None, "col": None, "orientation": None},
#     {"name": "Destroyer", "length": 3, "row": None, "col": None, "orientation": None},
#     {"name": "Battleship", "length": 4, "row": None, "col": None, "orientation": None},
#     {"name": "Carrier", "length": 5, "row": None, "col": None, "orientation": None},
# ]

# player1_ships: list[Ship] = []
# player1_ships = []
# player1_ships.append(Ship("Patrol Boat", 2))
# player1_ships.append(Ship("Submarine", 3))
# player1_ships.append(Ship("Destroyer", 3))
# player1_ships.append(Ship("Battleship", 4))
# player1_ships.append(Ship("Carrier", 5))

# for ship in player1_ships:
#     ship.place_ship()

#     display_grid(grid, player1_ships)
#     print()

# display_grid(grid)


# NALOGA

# Dopolnimo naš program tako, da mu dodamo class `Player`.

# Razred naj v sebi hrani:

# name - ime igralca
# grid - igralna plošča, na kateri bomo spremljali poteze katere je igralec naredil
# ships - list vseh igralčevih ladji
# create_grid - metoda, ki ustvari 2D list, ki predstavlja prazno igralno ploščo
# display_grid - metoda, ki izpiše igralčevo igralno ploščo. Na tej plošči bomo spremljali njegove poteze
# place_ship - metoda, ki prejme eno Ladjo in jo "postavi" na igralno ploščo
# display_my_ships - metoda, ki pokaže igralno ploščo in kje ima igralec postavljene ladje


class Player:
    def __init__(self, name):
        self.name = name
        self.grid = self.create_grid()
        self.ships = []
        self.ships.append(Ship("Patrol Boat", 2))
        # self.ships.append(Ship("Submarine", 3))
        # self.ships.append(Ship("Destroyer", 3))
        # self.ships.append(Ship("Battleship", 4))
        # self.ships.append(Ship("Carrier", 5))

        for ship in self.ships:
            self.place_ship(ship)

    def create_grid(self, n=10):
        grid = []
        # Prvi for loop za vrstice
        for row in range(n):
            empty_row = []
            # Drugi for loop za stolpce
            for col in range(n):
                empty_row.append("~")
            grid.append(empty_row)
        return grid

    def display_grid(self):
        print("R/C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(self.grid):
            print(i, end="   ")
            for col in row:
                print(col, end="  ")
            print()

    def place_ship(self, ship):
        print(f"Place a ship for player {self.name}")
        self.display_grid()
        ship.place_ship()
        for i in range(ship.length):
            if ship.orientation == "H":
                self.grid[ship.row][ship.col + i] = "S"
            elif ship.orientation == "V":
                self.grid[ship.row + i][ship.col] = "S"

    def display_my_ships(self):
        # This is used for debugging
        print(f"Displaying ships for player {self.name}")
        grid = self.create_grid()
        # grid # local
        # self.grid # instance varibale
        for ship in self.ships:
            for i in range(ship.length):
                if ship.orientation == "H":
                    self.grid[ship.row][ship.col + i] = "S"
                elif ship.orientation == "V":
                    self.grid[ship.row + i][ship.col] = "S"
        print("R/C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(self.grid):
            print(i, end="   ")
            for col in row:
                print(col, end="  ")
            print()


player1 = Player("Gregor")
print("=========")
player1.display_my_ships()
print("=========")
player1.display_grid()

player2 = Player("Anže")
print("=========")
player2.display_my_ships()
print("=========")
player2.display_grid()
