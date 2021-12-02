f = open("inputs", "r")                 # opens the file in f
lines = f.readlines()                   # loads all lines into lines as a string-array ['forward 4','down 8',.....]
depth = 0                               # initialize depth to 0
hor_pos = 0                             # initialize horizontal position to 0
for line in lines:                      # for each line in lines
    split_line = line.split(" ")        # splits a single line (e.g. 'forward 4' to an  string array at space (" ") -> line = ['forward','3']
    if split_line[0] == "forward":      # checks the split_line[0]
        hor_pos += int(split_line[1])   # handles the split_line[1] according to split_line[0] (same for the 2 elifs )
    elif split_line[0] == "down":
        depth += int(split_line[1])
    elif split_line[0] == "up":
        depth -= int(split_line[1])
print(depth * hor_pos)                  # prints the product of both values as asced