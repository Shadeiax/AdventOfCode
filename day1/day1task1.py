f = open("measures", "r")
lines = f.readlines()

counter = 0

for i in range(len(lines) - 1):
    if lines[i + 1] > lines[i]:
        counter += 1

    i += 1

print(counter)
