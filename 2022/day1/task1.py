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

print(max(elves), elves.index(max(elves))+1)