f = open("inputs", "r")
lines = f.readlines()
gamma = ""
epsilon = ""


def most_common_bit(index, list):
    count = 0
    for bin_string in list:
        if bin_string[index] == "0":
            count -= 1
        else:
            count += 1
    if count > 0:
        return "1"
    elif count < 0:
        return "0"
    else:
        print("Same amount on index", index)
        return "None"


for ind in range(len(lines[0]) - 1):
    com_bit = most_common_bit(ind, lines)
    gamma += com_bit
    epsilon += str(1 - int(com_bit))

print("g", gamma, "\ne", epsilon)
print(int(gamma, 2) * int(epsilon, 2))  # solution
