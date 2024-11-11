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


def display_grid(grid):
    print("R/C 0  1  2  3  4  5  6  7  8  9")
    for i, row in enumerate(grid):
        print(i, end="   ")
        for col in row:
            print(col, end="  ")
        print()


display_grid(grid)


def place_ship(grid, row=4, col=4, shipLength=5, orientation="V"):
    for i in range(shipLength):
        if orientation == "V":
            grid[row + i][col] = "S"
        elif orientation == "H":
            grid[row][col + i] = "S"


x = int(input("Vnesi x koordinato: "))
y = int(input("Vnesi y koordinato: "))
shipLength = int(input("Vnesi dolžino ladje: "))
orientacija = input("Vnesi orientacijo (V/H): ")
place_ship(grid, x, y, shipLength, orientacija)

display_grid(grid)
