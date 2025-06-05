mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

lights = [[x, y, 0] for y in range(1000) for x in range(1000)]
instructions = []
for line in input:
    line = line.split()
    if line[0] == "turn":
        line.remove("turn")
    line.remove("through")
    line[1] = int(line[1].split(",")[0]), int(line[1].split(",")[1])
    line[2] = int(line[2].split(",")[0]), int(line[2].split(",")[1])
    op, (x1, y1), (x2, y2) = line
    for light in lights:
        light_x, light_y, light_status = light
        if x1 <= light_x <= x2 and y1 <= light_y <= y2:
            if op == "on":
                light[2] += 1
            elif op == "off":
                light[2] -= 1
                if light[2] < 0:
                    light[2] = 0
            elif op == "toggle":
                light[2] += 2

res = sum(light[2] for light in lights)
print(res)
