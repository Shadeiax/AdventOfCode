mode = 2
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
        x = line.split(" ")
        x.remove(x[3])
        instructions.append(x)

instruction_index = 0
while len(instructions) > 0:
    gate1, operator, gate2, output = instructions[instruction_index]
    if gate1 in gates and gate2 in gates:
        gate1, gate2 = gates[gate1], gates[gate2]

        if operator == "AND":
            gates[output] = gate1 & gate2
        elif operator == "OR":
            gates[output] = gate1 | gate2
        elif operator == "XOR":
            gates[output] = gate1 ^ gate2

        instructions.pop(instruction_index)

    instruction_index += 1
    if instruction_index >= len(instructions):
        instruction_index = 0

z_gates = [gate for gate in gates if gate.startswith("z")]
z_gates.sort()
print(z_gates)

res = ""
for gate in z_gates:
    res = str(gates[gate]) + res
res_int = int(res)
res_dec = int(res, 2)

print(res_int)
print(res_dec)
