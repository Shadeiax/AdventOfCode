f = open("inputs", "r")
lines = f.readlines()
depth = 0
hor_pos = 0
aim = 0
for line in lines:
    split_line = line.split(" ")
    operation = split_line[0]
    amount = split_line[1]
    if operation == "forward":
        hor_pos += int(amount)
        depth += aim * int(amount)
    elif operation == "down":
        aim += int(amount)
    elif operation == "up":
        aim -= int(amount)
print(depth * hor_pos)