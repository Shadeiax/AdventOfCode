import math

mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


def parse_input(input):
    for line in input:
        if line.startswith("Register A:"):
            a = int(line.split(":")[1].strip())
        elif line.startswith("Register B:"):
            b = int(line.split(":")[1].strip())
        elif line.startswith("Register C:"):
            c = int(line.split(":")[1].strip())
        elif line.startswith("Program:"):
            instructions = [int(x) for x in line.split(":")[1].strip().split(",")]
    comp = ThreeBitComputer(a, b, c, instructions)
    return comp


class ThreeBitComputer:
    def __init__(self, reg_a, reg_b, reg_c, instructions):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.instructions = instructions
        self.instruction_pointer = 0
        self.output = []

    def compute(self):

        while self.instruction_pointer < len(self.instructions)-1:
            opcode = self.instructions[self.instruction_pointer]
            literal_operand = self.instructions[self.instruction_pointer + 1]
            if literal_operand == 4:
                combo_operand = self.reg_a
            elif literal_operand == 5:
                combo_operand = self.reg_b
            elif literal_operand == 6:
                combo_operand = self.reg_c
            else:
                combo_operand = literal_operand

            if opcode == 0:
                num = self.reg_a
                denom = 2 ^ combo_operand
                res = num / denom
                res = math.trunc(res)
                self.reg_a = res

            elif opcode == 1:
                # convert int to binary with 3 bits
                binary_b = str(bin(self.reg_b)[2:])
                binary_lit = str(bin(literal_operand)[2:])
                c = ""
                for x in range(3):
                    if binary_b[x] == binary_lit[x]:
                        c += "0"
                    else:
                        c += "1"
                res = int(c, 2)
                self.reg_b = res


            elif opcode == 2:
                res = combo_operand % 8
                self.reg_b = res

            elif opcode == 3:
                if self.reg_a == 0:
                    self.instruction_pointer = literal_operand

            elif opcode == 4:
                binary_b = str(bin(self.reg_b)[2:])
                binary_c = str(bin(self.reg_c)[2:])
                c = ""
                for x in range(3):
                    if binary_b[x] == binary_c[x]:
                        c += "0"
                    else:
                        c += "1"
                res = int(c, 2)
                self.reg_b = res

            elif opcode == 5:
                res = combo_operand % 8
                self.output.append(res)

            elif opcode == 6:
                num = self.reg_a
                denom = 2 ^ combo_operand
                res = num / denom
                res = math.trunc(res)
                self.reg_b = res

            elif opcode == 7:
                num = self.reg_a
                denom = 2 ^ combo_operand
                res = num / denom
                res = math.trunc(res)
                self.reg_c = res

            if opcode != 3:
                self.instruction_pointer += 2


computer = parse_input(input)
computer.compute()
print(computer.output)
print(computer.reg_b)