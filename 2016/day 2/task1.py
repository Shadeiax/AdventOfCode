mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]
print(input)

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

x,y = 1, 1
code = ""

for line in input:

    for char in line:
        if char == "U":
            y = max(0, y-1)
        elif char == "D":
            y = min(2, y+1)
        elif char == "L":
            x = max(0, x-1)
        elif char == "R":
            x = min(2, x+1)
    code += str(keypad[y][x])

print(code)