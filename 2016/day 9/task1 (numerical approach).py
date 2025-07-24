import re

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)][0]


def find_marker(string, start, end):
    return re.search(r"\((\d+)x(\d+)\)", string[start:end])

res = len(input)
markers = []
index = 0
while index < len(input):
    if input[index] == "(":
        marker = find_marker(input, index, len(input))
        length, repetitions = [int(x) for x in marker.group(1, 2)]
        skip = 3 + len(str(length)) + len(str(repetitions))
        res = res - skip + length * (repetitions - 1)
        index += length + skip

    else:
        index += 1

print(res)
