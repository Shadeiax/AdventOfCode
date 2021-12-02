f = open("inputs", "r")             # opens the file in f
lines = f.readlines()               # loads all lines into lines as a string-array ['forward 4','down 8',.....]
depth = 0                           # initialize depth to 0
hor_pos = 0                         # initialize horizontal position to 0
for line in lines:                  # for each line in lines
    split_line = line.split(" ")    # splits a single line (e.g. 'forward 4' to an  string array at space (" ")
                                    # -> line = ['forward','3']
    operation = split_line[0]       # assigns the first part of the line to operation
    amount = split_line[1]          # assigns the second part of the line to amount
    if operation == "forward":      # checks the operation
        hor_pos += int(amount)      # handles the amount according to operation (same for the 2 elifs )
    elif operation == "down":
        depth += int(amount)
    elif operation == "up":
        depth -= int(amount)
print(depth * hor_pos)              # prints the product of both values as asced