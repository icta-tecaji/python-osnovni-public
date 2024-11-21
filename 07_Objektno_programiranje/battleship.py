# Goal is to create a grid for a Battleship game and place ships on it.
# The grid should be a 10x10 2D list where each cell is initialized with "~".
# Example of a grid with ships placed on it:
# R/C 0  1  2  3  4  5  6  7  8  9
# 0   .  .  .  .  .  .  .  .  .  .
# 1   .  .  .  .  .  .  .  .  .  .
# 2   .  .  .  .  .  .  .  S  .  .
# 3   .  .  .  .  .  .  .  S  .  .
# 4   .  .  S  S  .  .  .  S  .  .
# 5   .  .  .  .  .  .  .  .  .  .
# 6   .  .  .  .  .  .  .  .  .  .
# 7   .  .  .  .  .  .  .  .  .  .
# 8   .  .  .  .  .  .  .  .  .  .
# 9   .  .  .  .  .  .  .  .  .  .

# Legend:
# ~ - water
# S - ship
# H - hit
# M - miss
# ```


def create_grid(n: int = 10) -> list:
    """Create a grid for the Battleship game.

    Args:
        n (int, optional): The size of the grid (number of rows and columns). Defaults to 10.

    Returns:
        list: A 2D list representing the grid, where each cell is initialized with "~".

    """
    grid = []
    # First loop for grid ROWS
    for row in range(n):
        empty_row = []  # We create an empty row
        # Second loop for grid COLUMNS
        for col in range(n):
            empty_row.append("~")  # We add a cell to the row each iteration
        grid.append(empty_row)
    return grid


grid = create_grid()


def display_grid(grid: list, ships: list) -> None:
    """Display the battleship grid with ships placed on it.

    Args:
        grid (list of list of str): A 2D list representing the grid where each cell is a string.
        ships (list of dict): A list of dictionaries where each dictionary represents a ship with the following keys:
            - "row" (int): The starting row of the ship.
            - "col" (int): The starting column of the ship.
            - "length" (int): The length of the ship.
            - "orientation" (str): The orientation of the ship, either "H" for horizontal or "V" for vertical.

    Returns:
        None

    """
    for ship in ships:  # Loop through the list of ships
        for i in range(ship["length"]):  # Loop through the length of the ship (E.g. 2 for Patrol Boat)
            if ship["orientation"] == "H":  # If the ship is oriented horizontally
                grid[ship["row"]][ship["col"] + i] = "S"  # Place the ship on the grid
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


# List of dictionaries representing the ships
# Each ship has the same keys.
# The values for "row", "col", and "orientation" are set to None
# This is a better practice than writing 0 for example, because 0 is a valid value for the row and column
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


# Fill in the program and place these ships on the grid:
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
