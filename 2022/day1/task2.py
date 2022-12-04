f = open("input", "r")
lines = f.readlines()

elves = []
sum = 0
for line in lines:
    if line != "\n":
        sum += int(line)
    else:
        elves.append(sum)
        sum = 0

elves.sort(reverse=True)
print(elves)
print(elves[0]+elves[1]+elves[2])
