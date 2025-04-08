input = [list(line.strip()) for line in open("input.txt")]

def find_guard(twod_array):
    for y, row in enumerate(twod_array):
        for x, char in enumerate(row):
            if char == "^":
                return y, x


def move_guard(twod_array, y, x):
    running = True
    old_y, old_x = y, x
    directions = ["^", ">", "v", "<"]
    while running:
        # calc new coordinates
        if twod_array[old_y][old_x] == "^":
            new_y, new_x = old_y - 1, old_x
        elif twod_array[old_y][old_x] == "v":
            new_y, new_x = old_y + 1, old_x
        elif twod_array[old_y][old_x] == ">":
            new_y, new_x = old_y, old_x + 1
        elif twod_array[old_y][old_x] == "<":
            new_y, new_x = old_y, old_x - 1

        # if exit
        if new_y < 0 or new_x < 0 or new_y >= len(twod_array) or new_x >= len(twod_array[0]):
            twod_array[old_y][old_x] = "X"
            running = False
        # check if obstacle
        elif twod_array[new_y][new_x] == "#":
            if directions.index(twod_array[old_y][old_x]) + 1 < 4:
                twod_array[old_y][old_x] = directions[directions.index(twod_array[old_y][old_x]) + 1]
            else:
                twod_array[old_y][old_x] = "^"

        # if valid move
        elif twod_array[new_y][new_x] == "." or twod_array[new_y][new_x] == "X":
            twod_array[new_y][new_x] = twod_array[old_y][old_x]  # Move guard to new position
            twod_array[old_y][old_x] = "X"  # Mark old guard position with "X"
            old_y, old_x = new_y, new_x

    return twod_array


def count_X(twod_array):
    count = 0
    for line in twod_array:
        count += line.count("X")
    return count


y, x = find_guard(input)

input = move_guard(input, y, x)
for line in input:
    print(line)
print(count_X(input))
