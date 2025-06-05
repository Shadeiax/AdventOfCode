from itertools import permutations

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

changes = []
names = set()
for line in input:
    line = line.split()
    person = line[0]
    names.add(person)
    next_to = line[10][:-1]
    if line[2] == "gain":
        value = int(line[3])
    elif line[2] == "lose":
        value = -int(line[3])
    changes.append((person, next_to, value))

for name in names:
    changes.append(("me", name, 0))
    changes.append((name, "me", 0))
names.add("me")

possible_seatings = [x for x in permutations(names)]

values = []
for seating in possible_seatings:
    change = 0
    for person in seating:
        for (change_person, next_to, value) in changes:
            if person == change_person and next_to == seating[(seating.index(person) + 1) % len(seating)]:
                change += value
            elif person == change_person and next_to == seating[(seating.index(person) - 1) % len(seating)]:
                change += value
    values.append(change)

print(max(values))
