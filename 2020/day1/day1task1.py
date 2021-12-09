f = open("input", "r")
lines = f.readlines()

for line in lines:
    rest = str(2020-int(line))+"\n"
    if rest in lines:
        print(int(rest)*(2020-int(rest)))
        break