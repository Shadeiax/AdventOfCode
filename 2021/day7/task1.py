f = open("input", "r")
lines = f.readlines()
nums = [int(x) for x in lines[0].split(",")]
nums.sort()

deltas = []

for num in nums:
    if num not in deltas:
        deltas.append(num)

lowest_cost = 0
lowest_delta = 0
for delta in deltas:
    cost = 0
    for num in nums:
        cost += abs(delta - num)
    if cost < lowest_cost or lowest_cost == 0:
        lowest_cost = cost
        lowest_delta = delta


print(lowest_delta,"with a cost of",lowest_cost)