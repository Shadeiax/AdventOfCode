from itertools import permutations

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

routes = []
cities = []
for line in input:
    line = line.split()
    line.pop(1)
    line.pop(2)
    routes.append(line)
    if line[0] not in cities:
        cities.append(line[0])
    if line[1] not in cities:
        cities.append(line[1])

possible_routes = [j for j in permutations(cities, len(cities))]

longest = 0
for curr_route in possible_routes:
    curr_weight = 0
    for index in range(len(curr_route) - 1):
        for route in routes:
            if (route[0] == curr_route[index] and route[1] == curr_route[index + 1]) or (
                    route[1] == curr_route[index] and route[0] == curr_route[index + 1]):
                curr_weight += int(route[2])
    if curr_weight > longest or longest == 0:
        longest = curr_weight

print(longest)
