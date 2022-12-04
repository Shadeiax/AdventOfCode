f = open("input", "r")
lines = f.readlines()


sum = 0
for line in lines:
    half1 = []
    half2 = []
    added = 0
    for i in range(len(line)):
        if i < len(line)/2-1:
            half1.append(line[i])
        else:
            half2.append(line[i])

    for j in range(len(half1)):
        if half1[j] in half2:
            common = half1[j]
            break

    if 64 < ord(common) < 91:
        added = ord(common) - 38
    else:
        added = ord(common) - 96
    sum += added

    print(common, added)
print(sum)