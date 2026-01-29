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
        for size in range(len(num_str)//2, 0, -1):
            chunks = [num_str[i:i + size] for i in range(0, len(num_str), size)]
            if len(num_str) % size == 0 and all(chunk == chunks[0] for chunk in chunks):
                res += i
                break
print(res)