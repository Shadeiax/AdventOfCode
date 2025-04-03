left = []
right = []

with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        left.append(line.split("   ")[0])
        right.append(line.split("   ")[1])

left.sort(), right.sort()
dist = 0

for i in range(len(left)):
    dist += abs(int(left[i]) - int(right[i]))

print(dist)
