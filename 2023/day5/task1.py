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

    results = []
    for seed in seeds:
        current = int(seed)
        for map in maps:
            for new, old, length in map:
                    if old <= current <= old + length-1:
                        current = new + current - old
                        break
        results.append(current)

print(min(results))