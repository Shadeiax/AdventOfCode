mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

instructions = [line.split() for line in input]
instructions2 = instructions.copy()



def process(instructions):
    gates = {}
    instruction_index = 0
    while len(instructions) > 0:
        instruction = instructions[instruction_index]
        if len(instruction) == 3:
            if instruction[0] in gates:
                gates[instruction[2]] = gates[instruction[0]]
                instructions.pop(instruction_index)
            elif instruction[0].isdigit():
                gates[instruction[2]] = int(instruction[0])
                instructions.pop(instruction_index)
        elif len(instruction) == 4:
            if instruction[1] in gates:
                # Perform NOT operation (16-bit)
                gates[instruction[3]] = ~gates[instruction[1]] & 0xFFFF
                instructions.pop(instruction_index)
        elif len(instruction) == 5:
            if instruction[0] in gates and instruction[2] in gates:
                if instruction[1] == "AND":
                    gates[instruction[4]] = gates[instruction[0]] & gates[instruction[2]]
                    instructions.pop(instruction_index)
                elif instruction[1] == "OR":
                    gates[instruction[4]] = gates[instruction[0]] | gates[instruction[2]]
                    instructions.pop(instruction_index)
            elif instruction[0] in gates and instruction[2].isdigit():
                if instruction[1] == "AND":
                    gates[instruction[4]] = gates[instruction[0]] & int(instruction[2])
                    instructions.pop(instruction_index)
                elif instruction[1] == "OR":
                    gates[instruction[4]] = gates[instruction[0]] | int(instruction[2])
                    instructions.pop(instruction_index)
                elif instruction[1] == "LSHIFT":
                    gates[instruction[4]] = gates[instruction[0]] << int(instruction[2])
                    instructions.pop(instruction_index)
                elif instruction[1] == "RSHIFT":
                    gates[instruction[4]] = gates[instruction[0]] >> int(instruction[2])
                    instructions.pop(instruction_index)
            elif instruction[0].isdigit() and instruction[2] in gates:
                if instruction[1] == "AND":
                    gates[instruction[4]] = int(instruction[0]) & gates[instruction[2]]
                    instructions.pop(instruction_index)
                elif instruction[1] == "OR":
                    gates[instruction[4]] = int(instruction[0]) | gates[instruction[2]]
        instruction_index += 1
        if instruction_index >= len(instructions):
            instruction_index = 0
    return gates



gates = process(instructions)

for instruction in instructions2:
    if len(instruction) == 3 and instruction[2] == "b":
        instruction[0] =str(gates["a"])

gates = process(instructions2)

print(*sorted(gates.items()), sep="\n", end="\n\n")
if "a" in gates:
    print(f"Result: {gates['a']}")
