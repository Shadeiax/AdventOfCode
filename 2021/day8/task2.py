f = open("example2", "r")
lines = f.readlines()

def decode(line):
    symbols = [[] for _ in range(10)]
    info = line.split("|")[0].strip().split()
    sequence = line.split("|")[1].strip().split()

    for part in info:
        if len(part) == 2:
            symbols[1] = part
        elif len(part) == 3:
            symbols[7] = part
        if len(part) == 4:
            symbols[4] = part
        elif len(part) == 7:
            symbols[8] = part
        else:
            pass

    for i,s in enumerate(symbols):
        print(i,s)

for line in lines:
    decode(line)