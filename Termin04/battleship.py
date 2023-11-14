class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.row = None
        self.col = None
        self.orientation = None
        self.demage = 0
        self.destroyed = False
        
    def place_ship(self):
        print(f"Placing ship {self.name} with length {self.length}")
        self.row = int(input("Row: "))
        self.col = int(input("Col: "))
        self.orientation = input("[H]orizontal / [V]ertical: ")

    def check_if_hit(self, row, col):
        ship_coordinates = []
        for i in range(self.length):
            if self.orientation == "H" or self.orientation == "h":
                ship_coordinates.append((self.row, self.col+i))
            elif self.orientation == "V" or self.orientation == "v":
                ship_coordinates.append((self.row+i, self.col))
        if (row, col) in ship_coordinates:
            self.demage += 1
            self.check_if_destroyed()
            return True
        else:
            return False
        
    def check_if_destroyed(self):
        if self.demage >= self.length:
            self.destroyed = True

class Player:
    def __init__(self, name):
        self.name = name
        self.grid = self.create_grid()
        self.ships = []
        #self.ships.append(Ship("Carrier", 5))
        #self.ships.append(Ship("Battleship", 4))
        #self.ships.append(Ship("Destroyer", 3))
        #self.ships.append(Ship("Submarine", 3))
        self.ships.append(Ship("Patrol Boat", 2))
        
        for ship in self.ships:
            self.place_ship(ship)
    
    def create_grid(self):
        # Creates empty grid
        grid = []
        for row in range(10):
            empty_row = []
            for col in range(10):
                empty_row.append(".")
            grid.append(empty_row)
        return grid
    
    def display_grid(self):
        print(f"Displaying grid for player {self.name}")
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
                if ship.orientation == "H" or ship.orientation == "h":
                    grid[ship.row][ship.col+i] = "S"
                elif ship.orientation == "V" or ship.orientation == "v":
                    grid[ship.row+i][ship.col] = "S"
        print("R/C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(grid):
            print(f"{i}   ", end="")
            for col in row:
                print(f"{col}", end="  ")
            print()

    def make_move(self, player2):
        print(f"{self.name}, make your move!")
        row = int(input("Row: "))
        col = int(input("Col: "))
        for ship in player2.ships:
            if ship.check_if_hit(row, col):
                print("HIT!")
                self.grid[row][col] = "H"
            else:
                print("MISS!")
                self.grid[row][col] = "M"

    def check_if_lost(self):
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

for _ in range(3):
    player1.make_move(player2)
    player1.display_grid()
    if player2.check_if_lost():
        print(f"{player1.name} Won!")
        break

    player2.make_move(player1)
    player2.display_grid()
    if player1.check_if_lost():
        print(f"{player2.name} Won!")
        break