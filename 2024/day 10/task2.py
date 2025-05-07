mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


def reformat(input):
    return [[char for char in line] for line in input]

def evaluate_trailheads(input: list[list[str]]) -> int:
    # find all trailheads
    trailheads = [(y, x) for y, line in enumerate(input) for x, spot in enumerate(line) if spot == "0"]

    # find routes for trailheads
    positions = trailheads.copy()
    for step in range(1, 10):
        step = str(step)
        new_positions = []
        for position in positions:
            y, x = position
            # check in all 4 directions
            new_positions.extend((y + dy, x + dx) for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                                 if 0 <= y + dy < len(input) and 0 <= x + dx < len(input[y])
                                 and input[y + dy][x + dx] == step)
        positions = new_positions.copy()
    return len(positions)


def listprint(list):
    print(*list, sep="\n", end="\n\n")


res = reformat(input)
listprint(res)
res = evaluate_trailheads(res)
print(res)
