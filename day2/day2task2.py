f = open("inputs", "r")
lines = f.readlines()
depth = 0
hor_pos = 0
aim = 0
for line in lines:
    split_line = line.split(" ")
    if split_line[0] == "forward":
        hor_pos += int(split_line[1])
        depth += aim * int(split_line[1])
    elif split_line[0] == "down":
        aim += int(split_line[1])
    elif split_line[0] == "up":
        aim -= int(split_line[1])
print(depth * hor_pos)