import numpy as np

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = np.array([line.strip() for line in open(file)])

res = 0
dial = 50

for line in input:
    dir = 1 if line[0] == "R" else -1
    for _ in range(int(line[1:])):
        dial += dir
        dial %= 100
        if dial == 0:
            res += 1



print("res:", res)
