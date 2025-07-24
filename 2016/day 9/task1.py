import re

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)][0]

res = ""
index = 0
while index < len(input):
    if input[index] == "(":
        marker = re.search(r"\((\d+)x(\d+)\)", input[index:])
        length, repetitions = [int(x) for x in marker.group(1, 2)]
        skip = 3 + len(str(length)) + len(str(repetitions))
        res += input[index + skip:index + skip + length] * repetitions
        index += length + skip

    else:
        res += input[index]
        index += 1

print(res)
print(len(res))
