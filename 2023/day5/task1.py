maps = []
current_map = []
with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        line = line.strip()
        if n == 0:
            seeds = line.split(":")[1].split()
        elif line.endswith(":"):
            current_map = []
        elif line == "":
            if current_map != []:
                maps.append(current_map)
        else:
            new, old, length = line.split()
            current_map.append((int(new), int(old), int(length)))
    maps.append(current_map)

    for ind, seed in enumerate(seeds):
        for map in maps:
            for new, old, length in map:
                if old <= int(seed) <= old + length-1:
                    seed = str(new + int(seed) - old)
                    break
            seeds[ind] = seed

print("------")
print(seeds)
print(min(seeds))

