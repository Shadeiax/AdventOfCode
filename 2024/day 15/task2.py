mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
inp = [line.strip() for line in open(file)]

field = []
instructions = []

read_mode = "field"
for line in inp:
    if line == "":
        read_mode = "instructions"
        continue
    if read_mode == "field":
        field.append(list(line))
    elif read_mode == "instructions":
        instructions.extend(line)

new_field = []
for line in field:
    new_line = []
    for char in line:
        if char == "#":
            new_line.extend("##")
        if char == "O":
            new_line.extend("[]")
        if char == ".":
            new_line.extend("..")
        if char == "@":
            new_line.extend("@.")
    new_field.append(new_line)
field = new_field

for y, line in enumerate(field):
    for x, char in enumerate(line):
        if char == "@":
            pos = y, x


def do_move(pos, move, field):
    y, x = pos
    next_y, next_x = (y + (move == "v") - (move == "^"), x + (move == ">") - (move == "<"))
    next = field[next_y][next_x]
    if next == ".":
        field[y][x], field[next_y][next_x] = field[next_y][next_x], field[y][x]
    elif next == "]":
        do_move((next_y, next_x), move, field)
        if move == "^" or move == "v":
            do_move((next_y, next_x - 1), move, field)
        do_move(pos, move, field)
    elif next == "[":
        do_move((next_y, next_x), move, field)
        if move == "^" or move == "v":
            do_move((next_y, next_x + 1), move, field)
        do_move(pos, move, field)

    return field, (next_y, next_x)


def check_move(pos, move, field):
    y, x = pos
    next_y, next_x = (y + (move == "v") - (move == "^"), x + (move == ">") - (move == "<"))
    # next_y, next_x = (y + (move == "v") - (move == "^"), x + (move == ">") - (move == "<"))
    next = field[next_y][next_x]
    if next == ".":
        return True
    elif next == "[":
        if move == "^" or move == "v":
            return check_move((next_y, next_x), move, field) and check_move((next_y, next_x + 1), move, field)
        else:
            return check_move((next_y, next_x), move, field)
    elif next == "]":
        if move == "^" or move == "v":
            return check_move((next_y, next_x), move, field) and check_move((next_y, next_x - 1), move, field)
        else:
            return check_move((next_y, next_x), move, field)
    else:
        return False


for move in instructions:
    if check_move(pos, move, field):
        field, pos = do_move(pos, move, field)

for line in field:
    print("".join(line))

# calc solution
gps_coordinate = 0
for y, line in enumerate(field):
    for x, char in enumerate(line):
        if char == "[":
            gps_coordinate += 100 * y + x

print(gps_coordinate)
