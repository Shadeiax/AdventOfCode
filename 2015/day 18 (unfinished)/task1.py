from itertools import product

mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

grid = []
for line in input:
    line = [char for char in line]
    grid.append(line)

for line in grid:
    print("".join(line))
print("")

new_grid = grid

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        neighbours = 0
        for (y_off, x_off) in list(product((0, -1, 1), repeat=2)):
            if (y_off, x_off) != (0, 0):
                if 0 <= (y + y_off) < len(grid) and 0 <= (x + x_off) < len(grid[0]):
                    if grid[y + y_off][x + x_off] == "#":
                        neighbours += 1
        if char == "#" and neighbours not in [2, 3]:
            new_grid[y][x] = "."
        elif char == "." and neighbours == 3:
            new_grid[y][x] = "#"


grid = new_grid

for line in grid:
    print("".join(line))
