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
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.row = None
        self.col = None
        self.orientation = None
        self.damage = 0

    def check_if_hit(self, row, col):
        ship_locations = []  # (row,col) in [(1,1), (1,2), (1,3)]
        for i in range(self.length):  # [0,1]
            if self.orientation.lower() == "h":
                ship_locations.append((self.row, self.col + i))
            if self.orientation.lower() == "v":
                ship_locations.append((self.row + 1, self.col))
        if (row, col) in ship_locations:
            self.damage += 1
            if self.damage >= self.length:
                print(f"Ship {self.name} is destroyed!")
            return True
        return False


# ---------------------------------------------------------------------------------------------------


class Submarine(Ship):
    def move(self):
        if self.orientation.lower() == "h":
            if (self.col + self.length + 1) > 10:
                self.col = 0
            else:
                self.col += 1
        if self.orientation.lower() == "v":
            if (self.row + self.length + 1) > 10:
                self.row = 0
            else:
                self.row += 1


# ---------------------------------------------------------------------------------------------------


class Player:
    def __init__(self, name):
        self.name = name
        self.grid = self.create_grid()  # where i already droped bombs
        self.ships = [
            Ship("Carrier", 5),
            Ship("Battleship", 4),
            Ship("Destroyer", 3),
            Ship("Submarine", 3),
            Ship("Petrol", 2),
            Submarine("Submarine", 3),
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

    def display_grid(self, grid_to_show=None):
        if grid_to_show is None:
            grid_to_show = self.grid
        print("R\\C 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(grid_to_show):
            row_to_print = str(i) + "   " + "  ".join(row)
            print(row_to_print)

    def place_ship(self, ship):
        print()
        print(f"Placing ship {ship.name} with length {ship.length}. (Player: {self.name})")
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

    def make_move(self, player2):
        # od playerja dobimo kam želi ciljati
        print(f"{self.name} making a move.")
        row = int(input("Row: "))
        col = int(input("Col: "))
        for ship in player2.ships:
            if ship.check_if_hit(row, col):
                print("HIT!")
                self.grid[row][col] = "H"
            else:
                print("Miss.")
                self.grid[row][col] = "M"
        for ship in player2.ships:
            if isinstance(ship, Submarine):
                ship.move()

    def check_if_lost(self):
        for ship in self.ships:
            if ship.damage < ship.length:
                return False
        return True


# ---------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # SET UP player1
    player1 = Player("Gregor")
    print("============")
    player1.display_my_ships()
    print("============")
    player1.display_grid()

    print()

    # SET UP player2
    player2 = Player("Anže")
    print("============")
    player2.display_my_ships()
    print("============")
    player2.display_grid()

    # ---------------------------------------------------------------------------------------------------

    for _ in range(10):
        player1.make_move(player2)
        player1.display_grid()
        player2.display_my_ships()
        if player2.check_if_lost():
            print("Player1 je zmagal!")
            break

        player2.make_move(player1)
        player2.display_grid()
        if player1.check_if_lost():
            print("Player2 je zmagal!")
            break
