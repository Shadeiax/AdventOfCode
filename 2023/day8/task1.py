

map = {}
with open("input", "r") as file:
    for index, line in enumerate(file.readlines()):
        if index == 0:
            instruction = line.strip()
        elif index > 1:
            position, directions = line.strip().split("=")
            position = position.strip()
            left, right = directions.split(",")
            left = left.strip().replace("(", "")
            right = right.strip().replace(")", "")
            map[position] = (left, right)

    print(map)
    found = False
    i = 0
    steps = 0
    pos = "AAA"
    while not found:
        if instruction[i] == "L":
            pos = map.get(pos)[0]
        elif instruction[i] == "R":
            pos = map.get(pos)[1]
        steps += 1
        i += 1
        if i > len(instruction) - 1:
            i = 0
        if pos == "ZZZ":
            found = True
    print(steps)
