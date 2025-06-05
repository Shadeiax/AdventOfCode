mode = 2
if mode == 1:
    file = "example.txt"
    time = 1000
elif mode == 2:
    time = 2503
    file = "input.txt"
input = [line.strip() for line in open(file)]

reindeers = {}
for line in input:
    line = line.split()
    reindeers[line[0]] = {"speed": int(line[3]), "time": int(line[6]), "rest": int(line[13]), "distance": 0}

for t in range(time):
    for reindeer in reindeers:
        if t % (reindeers[reindeer]["time"] + reindeers[reindeer]["rest"]) < reindeers[reindeer]["time"]:
            reindeers[reindeer]["distance"] += reindeers[reindeer]["speed"]

print(max(reindeers[reindeer]["distance"] for reindeer in reindeers))