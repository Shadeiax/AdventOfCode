import re

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


def has_aba(array):
    for entry in array:
        for i in range(len(entry) - 2):
            if entry[i] == entry[i + 2] and entry[i] != entry[i + 1]:
                return True
    return False


res = 0
for ip in input:
    hypernet = re.findall(r"\[(\w+)]", ip)
    rest = re.findall(r"(\w+)\[", ip) + re.findall(r"\](\w+)$", ip)

    if not has_aba(hypernet) and has_aba(rest):
        res += 1

print(res)

#490 too high
