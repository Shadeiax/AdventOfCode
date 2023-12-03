numbers = []
symbols = []
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
            elif char == ".":
                continue
            else:
                symbols.append((x, y))

    for n, (value, nxs, nxe, ny) in enumerate(numbers):
        for o, (sx, sy) in enumerate(symbols):
            if abs(sy-ny) <= 1:
                if abs(sx-nxs) <= 1 or abs(sx-nxe) <= 1:
                    solution+=int(value)
print(solution)