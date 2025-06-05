import re

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

pattern = r'-?\d+'
total = 0
for line in input:
    numbers = [int(n) for n in re.findall(pattern, line)]
    total += sum(numbers)
print(total)
