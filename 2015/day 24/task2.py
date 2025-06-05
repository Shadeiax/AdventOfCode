from itertools import combinations

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

nums = [int(n) for n in input]
target_sum = sum(nums) // 4
groups = []


def get_quantum_entanglement(group):
    x = 1
    for n in group:
        x *= n
    return x


def can_split_remaining(remaining, target_sum):
    for i in range(1, len(remaining)):
        for comb in combinations(remaining, i):
            if sum(comb) == target_sum:
                remaining2 = [x for x in remaining if x not in comb]
                if sum(remaining2) == 2*target_sum:
                    return True
    return False


for x in range(1, len(nums)):
    for group in combinations(nums, x):
        if sum(group) == target_sum:
            remaining = [n for n in nums if n not in group]
            if can_split_remaining(remaining, target_sum):
                groups.append(group)
    if groups:
        break

result = min(groups, key=get_quantum_entanglement)
print("Quantum entanglement:", get_quantum_entanglement(result))
