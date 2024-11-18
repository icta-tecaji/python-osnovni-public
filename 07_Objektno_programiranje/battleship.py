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


def create_grid(n=10):
    grid = []
    # Prvi for loop za vrstice
    for row in range(n):
        empty_row = []
        # Drugi for loop za stolpce
        for col in range(n):
            empty_row.append("~")
        grid.append(empty_row)
    return grid


grid = create_grid()


def display_grid(grid, ships):
    for ship in ships:
        for i in range(ship["length"]):
            if ship["orientation"] == "H":
                grid[ship["row"]][ship["col"] + i] = "S"
            elif ship["orientation"] == "V":
                grid[ship["row"] + i][ship["col"]] = "S"

    print("R/C 0  1  2  3  4  5  6  7  8  9")
    for i, row in enumerate(grid):
        print(i, end="   ")
        for col in row:
            print(col, end="  ")
        print()


def place_ship(ship: dict) -> dict:
    """Select the position for the ship.

    Args:
        ship (dict): A dictionary containing the ship's details, including its name.

    Returns:
        dict: The updated dictionary with the ship's position and orientation.
    Prompts the user to input the row, column, and orientation for the ship.

    """
    print(f"Placing ship {ship['name']}")

    ship["row"] = int(input("Vnesi vrstico: "))
    ship["col"] = int(input("Vnesi y koordinato: "))
    ship["orientation"] = input("Vnesi orientacijo (V/H): ")

    return ship


player1_ships = [
    {"name": "Patrol Boat", "length": 2, "row": None, "col": None, "orientation": None},
    {"name": "Submarine", "length": 3, "row": None, "col": None, "orientation": None},
    {"name": "Destroyer", "length": 3, "row": None, "col": None, "orientation": None},
    {"name": "Battleship", "length": 4, "row": None, "col": None, "orientation": None},
    {"name": "Carrier", "length": 5, "row": None, "col": None, "orientation": None},
]

for i, ship in enumerate(player1_ships):
    player1_ships[i] = place_ship(ship)

    display_grid(grid, player1_ships)
    print()

# display_grid(grid)


# Dopolnite program tako, da bo igralec postavil vse svoje ladjice.
#     Carrier, dolžina 5
#     Battleship, dolžina 4
#     Destroyer, dolžina 3
#     Submarine, dolžina 3
#     Patrol Boat, dolžina 2


# # Patrol ship - 2 tonka
# grid = place_ship(grid)
# display_grid(grid)

# # Submarine - 3 tonka
# grid = place_ship(grid)
# display_grid(grid)

# # Destroyer - 3 tonka
# grid = place_ship(grid)
# display_grid(grid)

# # Battleship - 4 tonka
# grid = place_ship(grid)
# display_grid(grid)

# # Carrier - 5 tonka
# grid = place_ship(grid)
# display_grid(grid)
