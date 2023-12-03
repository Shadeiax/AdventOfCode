f = open("input", "r")
lines = f.readlines()
dicts = []
sizes = []
current = None
previous = []
ls = False

for line in lines:
    if line.startswith("$") and ls:
        dicts.append([current, files])
        ls = False
    if line.startswith("$ cd"):
        if line.split()[2] == "..":
            current = previous[-1]
            previous.pop()
        else:
            previous.append(current)
            current = line.split()[2]
    elif line.startswith("$ ls"):
        files = []
        ls = True
    else:
        files.append([line.split()[0], line.split()[1]])
if ls:
    dicts.append([current, files])

for dict in dicts:

print(dicts)
