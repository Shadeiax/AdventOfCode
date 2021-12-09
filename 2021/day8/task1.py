f = open("input", "r")
lines = f.readlines()

counter = 0
accepted_lengths = [2, 3, 4, 7]
for line in lines:
    for symbol in line.split("|")[1].strip().split(" "):
        if len(symbol) in accepted_lengths:
            counter += 1


print(counter)
