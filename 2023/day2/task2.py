f = open("input", "r")
lines = f.readlines()

powers = []
for i, line in enumerate(lines, 1):
    false = False
    sets = line.split(":")[1].split(";")
    red_min = 0
    green_min = 0
    blue_min = 0
    for set in sets:
        colors = set.strip().split(",")
        for color in colors:
            color = color.split()
            if color[1] == "red" and int(color[0]) > red_min:
                red_min = int(color[0])
            elif color[1] == "green" and int(color[0]) > green_min:
                green_min = int(color[0])
            elif color[1] == "blue" and int(color[0]) > blue_min:
                blue_min = int(color[0])

    powers.append(red_min * green_min * blue_min)
answer = sum(powers)
print(answer)