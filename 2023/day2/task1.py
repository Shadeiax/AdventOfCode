f = open("input", "r")
lines = f.readlines()

answer = 0
for i, line in enumerate(lines, 1):
    false = False
    sets = line.split(":")[1].split(";")
    for set in sets:
        colors = set.strip().split(",")
        for color in colors:
            color = color.split()
            if color[1] == "red" and int(color[0]) > 12:
                false = True
            elif color[1] == "green" and int(color[0]) > 13:
                false = True
            elif color[1] == "blue" and int(color[0]) > 14:
                false = True
    if not false:
        answer+=i
        print(f"Game {i} counts")



print(answer)