import numpy as np

mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = np.array([line.strip() for line in open(file)])

res = 0
dial = 50

for line in input:
    dir = 1 if line[0] == "R" else -1
    dial = (dial + dir * int(line[1:])) % 100
    print(dial)
    if dial == 0:
        res += 1

print("res:", res)
