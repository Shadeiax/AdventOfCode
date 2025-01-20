
map = {}
with open("example", "r") as file:
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

    found = False
    i = 0
    steps = 0
    positions = [k for k in map.keys() if k.endswith("A")]
    print(positions)
    print([z for z in map.keys() if z.endswith("Z")])
    while not found:
        for pos_index, pos in enumerate(positions):
            if instruction[i] == "L":
                positions[pos_index] = map.get(pos)[0]
            elif instruction[i] == "R":
                positions[pos_index] = map.get(pos)[1]
        steps += 1
        i += 1
        if i > len(instruction) - 1:
            i = 0

        end_with_z = [z for z in positions if z.endswith("Z")]
        if len([z for z in positions if z.endswith("Z")]) == len(positions):
            found = True
    print(steps)

