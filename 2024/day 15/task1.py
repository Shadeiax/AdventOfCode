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

for y, line in enumerate(field):
    for x, char in enumerate(line):
        if char == "@":
            pos = y, x
            break


def do_move(pos, move, field):
    y, x = pos
    next_y, next_x = (y + (move == "v") - (move == "^"), x + (move == ">") - (move == "<"))
    next = field[next_y][next_x]
    if next == ".":
        field[y][x], field[next_y][next_x] = field[next_y][next_x], field[y][x]
    elif next == "O":
        do_move((next_y, next_x), move, field)
        do_move(pos, move, field)

    return field, (next_y, next_x)

def check_move(pos, move, field):
    y, x = pos
    next_y, next_x = (y + (move == "v") - (move == "^"), x + (move == ">") - (move == "<"))
    next = field[next_y][next_x]
    if next == ".":
        return True
    elif next == "O":
        return check_move((next_y, next_x), move, field)
    else:
        return False


for move in instructions:
    for line in field:
        print("".join(line))

    if check_move(pos, move, field):
        field, pos = do_move(pos, move, field)

gps_coordinate = 0
for y, line in enumerate(field):
    for x, char in enumerate(line):
        if char == "O":
            gps_coordinate += 100 * y + x

print(gps_coordinate)