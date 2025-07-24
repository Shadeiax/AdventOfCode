import numpy as np

mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = np.array([line.strip() for line in open(file)])
