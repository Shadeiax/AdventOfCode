mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

keypad = [
    ["#", "#", "1", "#", "#"],
    ["#", "2", "3", "4", "#"],
    ["5", "6", "7", "8", "9"],
    ["#", "A", "B", "C", "#"],
    ["#", "#", "D", "#", "#"]
]

x, y = 0, 2
code = ""

for line in input:
    for char in line:
        last = x,y
        if char == "U":
            y = max(0, y - 1)
        elif char == "D":
            y = min(4, y + 1)
        elif char == "L":
            x = max(0, x - 1)
        elif char == "R":
            x = min(4, x + 1)

        if keypad[y][x] == "#":
            x,y = last

    code += str(keypad[y][x])

print(code)
