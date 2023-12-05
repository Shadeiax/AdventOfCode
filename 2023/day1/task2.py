f = open("input", "r")
lines = f.readlines()

validt = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
validn = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0
for line in lines:
    finds = []
    for num in validn:
        if num in line:
            finds.append([validn.index(num) + 1, line.index(num)])
            if line.index(num) != line.rindex(num):
                finds.append([validn.index(num) + 1, line.rindex(num)])

    for num in validt:
        if num in line:
            finds.append([validt.index(num) + 1, line.index(num)])
            if line.index(num) != line.rindex(num):
                finds.append([validt.index(num) + 1, line.rindex(num)])

    finds.sort(key=lambda x: x[1])
    if len(finds) > 1:
        y = int(str(finds[0][0]) + str(finds[len(finds) - 1][0]))
    else:
        y = int(str(finds[0][0]) + str(finds[0][0]))
    sum += y

print(sum)
