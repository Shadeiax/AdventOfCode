from itertools import combinations

mode = 2
if mode == 1:
    file = "example.txt"
    goal = 25
elif mode == 2:
    file = "input.txt"#
    goal = 150
input = [line.strip() for line in open(file)]

containers = [int(line) for line in input]

res = 0
min = None
for container_amount in range(1, len(containers)+1):
    possible_combinations = list(combinations(containers, container_amount))
    for combination in possible_combinations:
        if sum(combination) == goal:
            if min == None:
                min = len(combination)
                res += 1
            elif len(combination) == min:
                res += 1

print(res)
