mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

gates = {}
instructions = []
reading = "gates"
for line in input:
    if line == "":
        reading = "instructions"
        continue
    if reading == "gates":
        name, value = line.split(":")[0], line.split(":")[1].strip()
        gates[name] = int(value)
    if reading == "instructions":
        print(line.split(" "))
        x = line.split(" ")
        x.remove(x[3])
        instructions.append(x)
