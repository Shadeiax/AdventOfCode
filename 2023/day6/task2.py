with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        if n == 0:
            times = line.strip().split(":")[1].replace(" ", "")

        elif n == 1:
            distances = line.strip().split(":")[1].replace(" ", "")
            races = [(int(times), int(distances))]

    print(races)
    race_results = []
    for time, distance in races:
        options = 0
        for hold_time in range(time):
            if (time - hold_time) * hold_time > distance:
                options += 1
        race_results.append(options)

    result = 1
    for x in range(len(race_results)):
        result *= race_results[x]

print(result)


