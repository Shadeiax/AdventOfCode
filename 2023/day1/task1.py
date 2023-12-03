f = open("input", "r")
lines = f.readlines()

sum = 0
for line in lines:
    finds = []
    for character in line:
        if character.isnumeric():
            finds.append([int(character), line.index(character)])

    sum += int(str(finds[0][0])+str(finds[len(finds)-1][0]))

print(sum)


