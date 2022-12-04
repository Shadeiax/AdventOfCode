f = open("input", "r")
lines = f.readlines()

count = 0
for line in lines:
    low_a, high_a, low_b, high_b = int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]), \
                                   int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]),

    if (low_a <= low_b and high_a >= high_b) or (low_a >= low_b and high_a <= high_b):
        count += 1

print(count)