f = open("input", "r")
lines = f.readlines()

i = 0
while i < len(lines[0]) - 3:
    marker = [lines[0][i], lines[0][i + 1], lines[0][i + 2], lines[0][i + 3]]
    print(marker)
    found = True
    for element in marker:
        if marker.count(element) > 1:
            found = False
    if found:
        print(i + 4)
        break
    i += 1
