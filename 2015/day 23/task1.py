mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
instructions = [line.strip().split() for line in open(file)]

a = 0
b = 0

print(instructions)

instruction_index = 0

while len(instructions) > instruction_index >= 0:
    instruction = instructions[instruction_index]
    if len(instruction) == 2:
        if instruction[0] == "hlf" and instruction[1] == "a":
            a = a // 2
            instruction_index += 1
        elif instruction[0] == "hlf" and instruction[1] == "b":
            b = b // 2
            instruction_index += 1
        elif instruction[0] == "tpl" and instruction[1] == "a":
            a = a * 3
            instruction_index += 1
        elif instruction[0] == "tpl" and instruction[1] == "b":
            b = b * 3
            instruction_index += 1
        elif instruction[0] == "inc" and instruction[1] == "a":
            a += 1
            instruction_index += 1
        elif instruction[0] == "inc" and instruction[1] == "b":
            b += 1
            instruction_index += 1
        elif instruction[0] == "jmp":
            instruction_index += int(instruction[1])

    elif len(instruction) == 3:
        if instruction[0] == "jie" and instruction[1][0] == "a":
            if a % 2 == 0:
                instruction_index += int(instruction[2])
            else:
                instruction_index += 1
        elif instruction[0] == "jie" and instruction[1][0] == "b":
            if b % 2 == 0:
                instruction_index += int(instruction[2])
            else:
                instruction_index += 1
        elif instruction[0] == "jio" and instruction[1][0] == "a":
            if a == 1:
                instruction_index += int(instruction[2])
            else:
                instruction_index += 1
        elif instruction[0] == "jio" and instruction[1][0] == "b":
            if b == 1:
                instruction_index += int(instruction[2])
            else:
                instruction_index += 1

print("a ", a)
print("b ", b)
