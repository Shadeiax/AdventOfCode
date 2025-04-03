left = []
right = []

with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1].replace("\n","")))

sim = 0

for i in range(len(left)):
    sim += right.count(left[i])*left[i]

print(sim)
