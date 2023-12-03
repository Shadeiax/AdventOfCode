f = open("input", "r")
lines = f.readlines()
i = 0
while i < len(lines[0]) - 15:
    marker = [c for c in lines[0][i:i + 15]]
    found = True
    for element in marker:
        if marker.count(element) > 1:
            found = False
    if found:
        print(i + 14)
        break
    i += 1
