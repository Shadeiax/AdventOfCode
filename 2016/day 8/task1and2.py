import numpy as np

mode = 2
if mode == 1:
    file = "example.txt"
    res = 7, 3
elif mode == 2:
    file = "input.txt"
    res = 50, 6
with open(file) as f:
    input = [line.strip() for line in f]

screen = [["." for _ in range(res[0])] for _ in range(res[1])]

screen = np.array(screen)


def rect(x, y):
    screen[0:y, 0:x] = "#"


def rotate_column(col, x):
    screen[:, col] = np.roll(screen[:, col], x)


def rotate_row(row, y):
    screen[row, :] = np.roll(screen[row, :], y)


for instruction in input:
    instruction = instruction.split()
    if instruction[0] == "rect":
        rect(int(instruction[1].split("x")[0]), int(instruction[1].split("x")[1]))
    elif instruction[0] == "rotate":
        if instruction[1] == "column":
            rotate_column(int(instruction[2].split("=")[1]), int(instruction[4]))
        elif instruction[1] == "row":
            rotate_row(int(instruction[2].split("=")[1]), int(instruction[4]))

print(*["".join(line) for line in screen], sep="\n")

screen = screen.reshape(-1)
print(len(np.where(screen == "#")[0]))
