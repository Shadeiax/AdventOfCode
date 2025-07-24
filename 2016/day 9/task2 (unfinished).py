import re

mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)][0]


def find_marker(string):
    return re.search(r"\((\d+)x(\d+)\)", string)

def find_all_markers(string):
    markers = []
    x = find_marker(string)
    if x:
        markers.append(x)
        return markers + find_all_markers(string[x.end():])
    else:
        return markers



res = len(input)
markers = []
index = 0
while index < len(input):
    if input[index] == "(":
        marker = find_marker(input[index:])
        print(marker)
        length, repetitions = [int(x) for x in marker.group(1, 2)]
        skip = 3 + len(str(length)) + len(str(repetitions))
        underlying_markers =  find_marker(input[index+skip:index+skip+length])
        print(underlying_markers)
        res = res - skip + length * (repetitions - 1)
        index += length + skip

    else:
        index += 1

print(res)
