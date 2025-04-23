mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [char for char in (line.strip() for line in open(file))]

new = []
for line in input:
    new.append([char for char in line])
input = new

antennas = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[x][y] != ".":
            antennas.append((input[x][y], x, y))
antennas.sort(key=lambda x: (x[0], x[1], x[2]))

antinodes = []
for ind1, antenna1 in enumerate(antennas):
    for ind2, antenna2 in enumerate(antennas):
        if ind1 == ind2:
            continue
        if antenna1[0] == antenna2[0]:
            x_dist = antenna1[1] - antenna2[1]
            y_dist = antenna1[2] - antenna2[2]
            new_x = antenna1[1] + x_dist
            new_y = antenna1[2] + y_dist
            if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
                continue
            elif [new_x, new_y] not in antinodes:
                    antinodes.append([new_x, new_y])

for a in antinodes:
    input[a[0]][a[1]] = "#"

print(len(antinodes))

