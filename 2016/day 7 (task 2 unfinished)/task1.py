import re

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


def has_abba(array):
    for entry in array:
        for i in range(len(entry) - 3):
            if entry[i] == entry[i + 3] and entry[i + 1] == entry[i + 2] and entry[i] != entry[i + 1]:
                return True
    return False


res = 0
for ip in input:
    hypernet = re.findall(r"\[(\w+)]", ip)
    rest = re.findall(r"(\w+)\[", ip) + re.findall(r"\](\w+)$", ip)

    if not has_abba(hypernet) and has_abba(rest):
        res += 1

print(res)
