f = open("input", "r")
lines = f.readlines()

index = 0
subindex = 0
while index < len(lines)-1:
    num1 = lines[index]
    while subindex < len(lines)-1:
        num2 = lines[subindex]
        rest = str(2020 - int(num1) - int(num2)) + "\n"
        if rest in lines:
            print(int(rest) * int(num1) * int(num2))
            break
        else:
            subindex += 1
    index += 1
    subindex = index

