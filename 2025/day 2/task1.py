import numpy as np

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = np.array([line.strip() for line in open(file)])

ids = input[0].split(",")
ranges = [rng.split("-") for rng in ids]
res = 0
for rng in ranges:
    for i in range(int(rng[0]), int(rng[1])+1):
        num_str = str(i)
        if len(num_str) % 2 == 0:
            half_length = len(num_str) // 2
            first_half = num_str[:half_length]
            second_half = num_str[-half_length:]
            if first_half == second_half:
                res += i
print(res)