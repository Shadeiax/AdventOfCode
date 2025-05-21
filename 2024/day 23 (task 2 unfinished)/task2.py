from itertools import combinations

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

connections = [(line.split("-")[0], line.split("-")[1]) for line in input]


def check_if_valid(needed_connections, connections):
    for connection in needed_connections:
        if not (connection in connections or (connection[1], connection[0]) in connections):
            return False
    return True


pcs = set()
for connection in connections:
    pcs.add(connection[0])
    pcs.add(connection[1])

for x in range(3, len(pcs)):
    found = False
    possible_networks = set(combinations(pcs, x))
    for network in possible_networks:
        needed_connections = list(combinations(network, 2))
        if check_if_valid(needed_connections, connections):
            print("Found a network with", x, "pcs")
            print(network)
            print(needed_connections)
            valid_network = network
            found = True
            break
    if not found:
        break

valid_network = sorted(valid_network)
print("Valid network:", valid_network)

print(*valid_network, sep=",")
