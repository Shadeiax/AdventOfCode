import re

mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


long = 0
short = 0
for line in input:
    slash = re.findall(r"\\", line)
    escaped = re.findall(r"\\\\", line)
    hexes = re.findall(r"\\x..", line)
    long += len(line)
    short += len(line) - (len(slash)-len(hexes)) - len(escaped) - 3*len(hexes) - 2

res = long - short
print(res)