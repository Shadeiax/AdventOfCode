mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

input = input[0].split(", ")

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
pos = 0, 0
direction = 0, 1
visited = []

broken = False
for instruction in input:
    turn = instruction[0]
    distance = int(instruction[1:])

    turn_index = directions.index(direction)
    if turn == "L":
        turn_index = (turn_index - 1) % 4
    elif turn == "R":
        turn_index = (turn_index + 1) % 4
    direction = directions[turn_index]

    for x in range(distance):
        pos = pos[0] + directions[turn_index][0], pos[1] + directions[turn_index][1]
        if pos in visited:
            print(pos)
            broken = True
            break
        visited.append(pos)
    if broken:
        break

res = sum([abs(val) for val in pos])
print(res)
