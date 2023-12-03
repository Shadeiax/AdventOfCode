numbers = []
gears = []
solution = 0

with open("input", "r") as file:
    for y, line in enumerate(file.readlines()):
        reading = ""
        num_start = None
        for x, char in enumerate(line.strip()):
            if char.isnumeric():
                reading += char
                if num_start is None:
                    num_start = x
                if not line[x+1].isnumeric():
                    numbers.append((reading, num_start, x, y))
                    reading = ""
                    num_start = None
            elif char == "*":
                gears.append((x, y))
    for n, (gx ,gy) in enumerate(gears):
        adjacent = []
        for o, (value, nxs, nxe, ny) in enumerate(numbers):
            if abs(gy - ny) <= 1:
                if abs(gx - nxs) <= 1 or abs(gx - nxe) <= 1:
                    adjacent.append(int(value))
        if len(adjacent) == 2:
            solution+=(adjacent[0]*adjacent[1])
print(solution)