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


class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.row = None
        self.col = None
        self.orientation = None
        self.damage = 0
        self.destroyed = False

    def place_ship(self):
        print(f"Placing ship {self.name} ({self.length})")

        self.row = int(input("Vnesi vrstico: "))
        self.col = int(input("Vnesi stolpec: "))
        self.orientation = input("Vnesi orientacijo (V/H): ")

    def check_if_hit(self, row, col):
        ship_coordiantes = []
        for i in range(self.length):
            if self.orientation == "H":
                ship_coordiantes.append((self.row, self.col + i))
            elif self.orientation == "V":
                ship_coordiantes.append((self.row + i, self.col))

        # preverimo e je (row, col) znotraj koordiante ladje
        if (row, col) in ship_coordiantes:
            # Če je: updateamo ladjo +1 damage + vrnemo True
            self.damage += 1
            self.check_if_destroyed()
            return True
        # Če ni: vrnemo False
        return False

    def check_if_destroyed(self):
        if self.damage >= self.length:
            self.destroyed = True


class Submarine(Ship):
    def move(self):
        if self.orientation == "H":
            # <True> if <condition> else <False>
            self.col = 0 if (self.col + self.length) >= 10 else self.col + 1
        elif self.orientation == "V":
            # <True> if <condition> else <False>
            self.row = 0 if (self.row + self.length) >= 10 else self.row + 1


# ======================================================================================
# ======================================================================================
# ======================================================================================
# ======================================================================================
# ======================================================================================
# ======================================================================================
# ======================================================================================


class Player:
    def __init__(self, name):
        self.name = name
        self.grid = self.create_grid()
        self.ships = []
        self.ships.append(Ship("Patrol Boat", 2))
        self.ships.append(Submarine("Submarine", 3))
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
        print(f"Displaying grid of player {self.name}")
        print("R/C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(self.grid):
            print(i, end="   ")
            for col in row:
                print(col, end="  ")
            print()

    def place_ship(self, ship):
        print(f"Place a ship for player {self.name}")
        self.display_my_ships()
        ship.place_ship()

    def display_my_ships(self):
        # This is used for debugging
        print(f"Displaying ships for player {self.name}")
        grid = self.create_grid()
        # grid # local
        # self.grid # instance varibale
        for ship in self.ships:
            for i in range(ship.length):
                if ship.orientation == "H":
                    grid[ship.row][ship.col + i] = "S"
                elif ship.orientation == "V":
                    grid[ship.row + i][ship.col] = "S"
        print("R/C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(grid):
            print(i, end="   ")
            for col in row:
                print(col, end="  ")
            print()

    def make_move(self, other_player):
        # inputi za kam želi vrči bombo
        print(f"{self.name} making a move.")
        row = int(input("Row:"))
        col = int(input("Col:"))
        # preverimo ali je zadetek
        for ship in other_player.ships:
            # pogledamo če je zadetek
            if ship.check_if_hit(row, col):
                # Če je: shranimo v svoj grid "H"
                self.grid[row][col] = "H"
                print("HIT!")
            else:
                # Če ni: shranimo v svoj grid "M"
                self.grid[row][col] = "M"
                print("Miss.")
        for ship in self.ships:
            if ship.name == "Submarine":
                ship.move()

    def check_if_loss(self):
        for ship in self.ships:
            if not ship.destroyed:
                return False
        return True


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


print("*" * 10)
print("*" * 10)
print("*" * 10)
print("*" * 10)


for _ in range(3):
    player1.make_move(player2)
    player1.display_grid()
    player1.display_my_ships()

    if player2.check_if_loss():
        # player1 je zmagovalec
        print(f"Player {player1.name} WON!")
        break

    player2.make_move(player1)
    player2.display_grid()

    if player1.check_if_loss():
        # player2 je zmagovalec
        print(f"Player {player2.name} WON!")
        break
