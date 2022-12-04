f = open("input", "r")
lines = f.readlines()

sum = 0

badge_commons = []

i = 0
while i < len(lines)-1:
    line1 = lines[i]
    line2 = lines[i+1]
    line3 = lines[i+2]
    for char in line1:
        if char in line2 and char in line3:
            badge_commons.append(char)
            break
    i += 3

for common in badge_commons:
    if 64 < ord(common) < 91:
        added = ord(common) - 38
    else:
        added = ord(common) - 96
    sum += added
    print(common)

print(sum)