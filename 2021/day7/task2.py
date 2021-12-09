f = open("input", "r")
lines = f.readlines()
nums = [int(x) for x in lines[0].split(",")]
nums.sort()

deltas = [x for x in range(max(nums))]

lowest_cost = 0
lowest_delta = 0
for delta in deltas:
    print(delta, "/", max(nums))
    cost = 0
    for num in nums:
        steps = abs(delta - num)
        step_cost = 0
        for i in range(steps):
            step_cost += i + 1
        cost += step_cost
    if cost < lowest_cost or lowest_cost == 0:
        lowest_cost = cost
        lowest_delta = delta

print(lowest_delta, "with a cost of", lowest_cost)
