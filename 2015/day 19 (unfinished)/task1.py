mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

replacements = []
for line in input[:-2]:
    line = line.split("=>")
    replacements.append((line[0].strip(), line[1].strip()))
input = input[-1].strip()
print(replacements)
print(input)
molecules = []
for replacement in replacements:
    indeces = [x for x, char in enumerate(input) if char == replacement[0]]
    for index in indeces:
        molecules.append(input[0:index]+replacement[1]+input[index+1:])

#print(molecules)
print(len(molecules))
print(len(set(molecules)))

#189 too low
#213 too low
