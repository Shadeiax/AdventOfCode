mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


def reformat(input):
    return [[char for char in line] for line in input]


def evaluate_trailheads(input):
    # find all trailheads
    trailheads = set()
    for y, line in enumerate(input):
        for x, spot in enumerate(line):
            if spot == "0":
                trailheads.add((y, x))

    sum = 0
    for trailhead in trailheads:
        # find routes for trailheads
        positions = [trailhead]
        for step in range(1, 10):
            step = str(step)
            new_positions = set()
            for position in positions:
                y, x = position
                # check in all 4 directions
                new_positions.update((y + dy, x + dx) for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                                     if 0 <= y + dy < len(input) and 0 <= x + dx < len(input[y])
                                     and input[y + dy][x + dx] == step)
            positions = new_positions.copy()
        sum += len(positions)
    return sum


def listprint(list):
    for i in range(len(list)):
        print(list[i], end="\n")
    print()


res = reformat(input)
listprint(res)
res = evaluate_trailheads(res)
print(res)
