# https://shorturl.at/klBFW
class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.row = None
        self.col = None
        self.orientation = None
        self.damage = 0

    def place_ship(self):
        print(f"Placing ship {self.name} with length {self.length}")
        self.row = int(input("Row: "))
        self.col = int(input("Col: "))
        self.orientation = input("[H]orizontal / [V]ertical: ")

    def check_if_hit(self, row, col):
        ship_coordinates = []
        for i in range(self.length):
            if self.orientation == "H":
                ship_coordinates.append((self.row, self.col + i))
            elif self.orientation == "V":
                ship_coordinates.append((self.row + i, self.col))
        if (row, col) in ship_coordinates:
            self.damage += 1
            return True
        else:
            return False


class Player:
    def __init__(self, name):
        self.name = name
        self.grid = self.create_grid()
        self.ships = []
        self.ships.append(Ship("Patrol Boat", 2))
        # todo - dodaj še preostale ladje

        for ship in self.ships:
            self.place_ship(ship)

    def create_grid(self):
        """
        . -> empty field
        S -> ship piece
        H -> hit
        M -> miss
        """
        grid = []
        for row in range(10):
            empty_row = []
            for col in range(10):
                empty_row.append(".")
            grid.append(empty_row)
        return grid

    def display_grid(self):
        print(f"Displaying grifd for player {self.name}")
        print("R/C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(self.grid):
            print(f"{i}   ", end="")
            for col in row:
                print(f"{col}", end="  ")
            print()

    def place_ship(self, ship):
        print(f"Placing a ship for player {self.name}")
        self.display_my_ships()
        ship.place_ship()

    def display_my_ships(self):
        print(f"Displaying ships for player {self.name}")
        grid = self.create_grid()

        for ship in self.ships:
            for i in range(ship.length):
                if ship.orientation == "H":
                    grid[ship.row][ship.col + i] = "S"
                elif ship.orientation == "V":
                    grid[ship.row + i][ship.col] = "S"
        print("R/C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(grid):
            print(f"{i}   ", end="")
            for col in row:
                print(f"{col}", end="  ")
            print()

    def make_move(self, player2):
        print(f"{self.name} is making a move.")
        row = int(input("Row: "))
        col = int(input("Col: "))
        for ship in player2.ships:
            if ship.check_if_hit(row, col):
                print("HIT!")
                self.grid[row][col] = "H"
            else:
                print("Miss.")
                self.grid[row][col] = "M"


player1 = Player("Gregor")
print(30 * "=")
player1.display_my_ships()
print(30 * "=")
player1.display_grid()

player2 = Player("Anže")
print(30 * "=")
player2.display_my_ships()
print(30 * "=")
player2.display_grid()

for _ in range(3):
    player1.make_move(player2)
    player1.display_grid()
