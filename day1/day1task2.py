f = open("measures", "r")
lines = f.readlines()
counter = 0
for i in range(len(lines) - 3):
    group1 = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    group2 = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3])
    print(group1, group2)
    if group2 > group1:
        counter += 1
    i += 1
print(counter)
