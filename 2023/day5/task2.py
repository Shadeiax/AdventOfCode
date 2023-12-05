maps = []
with open("example", "r") as file:
    for n, line in enumerate(file.readlines()):
        line = line.strip()
        if line == "":
            continue
        elif n == 0:
            seeds = line.split(":")[1].split()
        elif line.endswith(":"):
            for ind, seed in enumerate(seeds):
                for new, old, length in maps:
                    if old <= int(seed) <= old + length - 1:
                        seed = str(new + int(seed) - old)
                        break
                seeds[ind] = seed
            maps = []
        else:
            new, old, length = line.split()
            maps.append((int(new), int(old), int(length)))

print(seeds)
print(min(seeds))
