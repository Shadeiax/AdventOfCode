f = open("input", "r")
lines = f.readlines()

moving = False
stacks = []
setup_lines = []
for line in lines:
    if line == "\n":
        for x in range(len(setup_lines[-1])):
            stacks.append([])

        for x in range(len(setup_lines[-1])):
            for line in setup_lines[:-1]:
                if len(line) > x and line[x] != '':
                    stacks[x].insert(0, line[x].strip("[]"))

        moving = True

    elif moving == False:
        setup_lines.append([line[i:i + 4].strip() for i in range(0, len(line), 4)])


    elif moving == True:
        line = line.split()
        amount, start, end = int(line[1]), int(line[3])-1, int(line[5])-1
        print(stacks)
        crates = stacks[start][-amount:]#
        crates.reverse()
        print(crates)
        for crate in crates:
            stacks[end].append(crate)
        stacks[start] = stacks[start][:-amount]
        print(stacks,"\n")

solution = ""
for stack in stacks:
    solution+=str(stack[-1])
print(solution)