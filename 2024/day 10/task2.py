mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


def reformat(input):
    new = []
    for line in input:
        new_line = []
        for char in line:
            new_line.append(char)
        new.append(new_line)
        new_line = []
    return new


def evaluate_trailheads(input):
    # find all trailheads
    trailheads = []
    for y, line in enumerate(input):
        for x, spot in enumerate(line):
            if spot == "0":
                trailheads.append((y, x))


    # find routes for trailheads
    positions = trailheads.copy()
    for step in range(1, 10):
        step = str(step)
        new_positions = []
        for position in positions:
            y, x = position
            # check in all 4 directions
            if y < len(input) - 1:
                if input[y + 1][x] == step:
                    new_positions.append((y + 1, x))
            if y > 0:
                if input[y - 1][x] == step:
                    new_positions.append((y - 1, x))
            if x < len(input[y]) - 1:
                if input[y][x + 1] == step:
                    new_positions.append((y, x + 1))
            if x > 0:
                if input[y][x - 1] == step:
                    new_positions.append((y, x - 1))
        positions = new_positions.copy()

    return len(positions)


def listprint(list):
    for i in range(len(list)):
        print(list[i], end="\n")
    print()


res = reformat(input)
listprint(res)
res = evaluate_trailheads(res)
print(res)
