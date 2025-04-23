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
            x = antenna1[1]
            y = antenna1[2]
            while True:
                new_x = x + x_dist
                new_y = y + y_dist
                if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
                    break
                elif [new_x, new_y] not in antinodes and input[new_y][new_x] == ".":
                    antinodes.append([new_x, new_y])
                x, y = new_x, new_y

count = 0
for a in antinodes:
    if input[a[0]][a[1]] == ".":
        input[a[0]][a[1]] = "#"
        count += 1

for line in input:
    l = ""
    for char in line:
        l += char
    print(l)

print(count + len(antennas))
