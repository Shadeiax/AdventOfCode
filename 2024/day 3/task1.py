import re

mults = []

with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        mults += (re.findall("mul\(\d+,\d+\)", line))

print(mults)

prod = 0
for mult in mults:
    a = mult.split("(")[1].split(",")[0]
    b = mult.split(",")[1].split(")")[0]
    prod += int(a) * int(b)

print(prod)
