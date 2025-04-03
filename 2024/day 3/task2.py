import re

instructions = []

with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        instructions += (re.findall("(mul\(\d+,\d+\)|do\(\)|don't\(\))", line))

print(instructions)

prod = 0
on = True
for inst in instructions:
    if inst == "do()":
        on = True
    elif inst == "don't()":
        on = False
    elif on:
        a = inst.split("(")[1].split(",")[0]
        b = inst.split(",")[1].split(")")[0]
        prod += int(a) * int(b)

print(prod)
