f = open("input", "r")
lines = f.readlines()

count = 0
for line in lines:
    low_a, high_a, low_b, high_b = int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]), \
                                   int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]),

    range1 = list(range(low_a, high_a + 1))
    range2 = list(range(low_b, high_b + 1))

    for num in range1:
        if num in range2:
            count += 1
            break

print(count)
