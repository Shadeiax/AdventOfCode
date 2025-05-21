from itertools import combinations

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

connections = [(line.split("-")[0], line.split("-")[1]) for line in input]


pcs = set()
for connection in connections:
    pcs.add(connection[0])
    pcs.add(connection[1])

combinations = list(combinations(pcs, 3))
combinations = [combination for combination in combinations if (
        combination[0].startswith("t") or combination[1].startswith("t") or combination[2].startswith("t"))]

print(len(combinations))
interconnected_combinations = [combination for combination in combinations if (
        ((combination[0], combination[1]) in connections or (combination[1], combination[0]) in connections) and
        ((combination[0], combination[2]) in connections or (combination[2], combination[0]) in connections) and
        ((combination[1], combination[2]) in connections or (combination[2], combination[1]) in connections))]


intercon_combs_with_t = [combination for combination in interconnected_combinations if (
        combination[0].startswith("t") or combination[1].startswith("t") or combination[2].startswith("t"))]

print(len(intercon_combs_with_t))