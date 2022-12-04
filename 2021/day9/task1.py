f = open("example", "r")
lines = f.readlines()


grid = []
for line in lines:
    line = line.strip()
    grid_line = []
    for charac in line:
        grid_line.append(int(charac))
    grid.append(grid_line)



risk_level = 0



print(risk_level)


