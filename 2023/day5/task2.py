maps = []
current_map = []
seeds = []
with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        line = line.strip()
        if n == 0:
            a = line.split(":")[1].split()
            ranges = []
            for x in range(len(a)):
                if x % 2 == 0:
                    ranges.append((int(a[x]), int(a[x])+int(a[x+1])-1))


            for start,stop in ranges:
                ind = 0
                while ind <= stop:
                    seeds.append(start+ind)
                    ind += 1



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