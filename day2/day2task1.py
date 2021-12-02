f = open("inputs", "r")
lines = f.readlines()
depth = 0
hor_pos = 0
for line in lines:
    split_line = line.split(" ")
    operation = split_line[0]
    amount = split_line[1]
    if operation == "forward":
        hor_pos += int(amount)
    elif operation == "down":
        depth += int(amount)
    elif operation == "up":
        depth -= int(amount)
print(depth * hor_pos)