# potapljanje ladjic 10x10

# R\C 0 1 2 3 4 5 6 7 8 9
# 0   . . . . . . . . . .
# 1   . . . . . . . . . .
# 2   . . . . . . . . . .
# 3   . . . . . . . . . .
# 4   . . . . . . . . . .
# 5   . . . . . . . . . .
# 6   . . . . . . . . . .
# 7   . . . . . . . . . .
# 8   . . . . . . . . . .
# 9   . . . . . . . . . .

# . - prazno polje/morje
# S - 1 kos ladje
# H - "hit" oz. zadetek
# M - "miss" oz. smo streljali in zgrešili


# ---------------------------------------------------------------------------------------------------
class Ship:
    def __init__(self,name,length):
        self.name = name
        self.length = length
        self.row = None
        self.col = None
        self.orientation = None

    def place_ship(self):
        print()
        print(f"Placing ship {self.name} with length {self.length}.")
        self.row = int(input("Row: "))
        self.col = int(input("Col: "))
        self.orientation = input("[H]orizontal / [V]ertical: ").strip()

# ---------------------------------------------------------------------------------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.grid = self.create_grid()
        self.ships = [
            # Ship("Carrier",5),
            # Ship("Battleship",4),
            # Ship("Destroyer",3),
            # Ship("Submarine",3),
            Ship("Petrol",2)
        ]

        for ship in self.ships:
            self.place_ship(ship)

    def create_grid(self):
        # Create empy grid
        grid = []
        for row in range(10):
            empty_row = []
            for col in range(10):
                empty_row.append(".")
            grid.append(empty_row)
        return grid

    def display_grid(self,grid=None):
        if grid is None:
            grid = self.grid
        print("R\\C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(self.grid):
            row_to_print = str(i) + "   " + "  ".join(row)
            print(row_to_print)

    def place_ship(self,ship):
        print()
        print(f"Placing ship {ship.name} with length {ship.length}.")
        ship.row = int(input("Row: "))
        ship.col = int(input("Col: "))
        ship.orientation = input("[H]orizontal / [V]ertical: ").strip()

    def display_my_ships(self):
        print()
        print(f"Displaying ships for player {self.name}.")
        grid = self.create_grid()
        
        for ship in self.ships:
            for i in range(ship.length):
                if ship.orientation.lower() == "h":
                    grid[ship.row][ship.col + i] = "S"
                if ship.orientation.lower() == "v":
                    grid[ship.row + i][ship.col] = "S"
        self.display_grid(grid)
        



# ---------------------------------------------------------------------------------------------------


player1 = Player("Gregor")
print("============")
player1.display_my_ships()
print("============")

player2 = Player("Anže")
print("============")
player2.display_my_ships()
print("============")




grid = create_grid()
display_grid(grid, [])


# player1_ships = [
#     # {"name": "Carrier", "length": 5, "row": None, "col": None, "orientation": None},
#     # {"name": "Battleship", "length": 4, "row": None, "col": None, "orientation": None},
#     # {"name": "Destroyer", "length": 3, "row": None, "col": None, "orientation": None},
#     # {"name": "Submarine", "length": 3, "row": None, "col": None, "orientation": None},
#     {"name": "Petrol", "length": 2, "row": 3, "col": 4, "orientation": "H"},
# ]

player1_ships = [
    # Ship("Carrier",5),
    # Ship("Battleship",4),
    # Ship("Destroyer",3),
    # Ship("Submarine",3),
    Ship("Petrol",2)
]


for ship in player1_ships:
    ship.place_ship()
    display_grid(grid,player1_ships)

display_grid(grid, player1_ships)
