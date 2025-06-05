mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

sues = []
for line in input:
    line = line.split()
    name, number, gift1, value1, gift2, value2, gift3, value3 = line
    number = number[:-1]
    gift1 = gift1[:-1]
    gift2 = gift2[:-1]
    gift3 = gift3[:-1]
    value1 = value1[:-1]
    value2 = value2[:-1]
    line = name, number, gift1, value1, gift2, value2, gift3, value3
    sue = {"number":number, gift1: int(value1), gift2: int(value2), gift3: int(value3)}
    sues.append(sue)

ticker = {"children": 3,
          "cats": 7,
          "samoyeds": 2,
          "pomeranians": 3,
          "akitas": 0,
          "vizslas": 0,
          "goldfish": 5,
          "trees": 3,
          "cars": 2,
          "perfumes": 1}


for sue in sues:
    found = True
    for item in sue:
        if item != "number":
            if item == "cats" or item == "trees":
                if sue[item] <= ticker[item]:
                    found = False
                    break
            elif item == "pomeranians" or item == "goldfish":
                if sue[item] >= ticker[item]:
                    found = False
                    break
            else:
                if sue[item] != ticker[item]:
                    found = False
                    break
    if found:
        print(sue["number"])