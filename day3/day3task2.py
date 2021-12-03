f = open("inputs", "r")
lines = f.readlines()
oxygen_generator_rating = lines
CO2_scrubber_rating = lines


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


def solve(list, preferred, flip):
    keep = []
    index = 0
    while len(list) > 1:
        com_bit = most_common_bit(index, list)
        if com_bit == "None":
            com_bit = preferred
        elif flip == True:
            com_bit = str(1 - int(com_bit))
        for line in list:
            if line[index] == com_bit:
                keep.append(line)
        list = keep
        keep = []
        index += 1
    print(int(list[0], 2))
    return int(list[0], 2)


print(solve(oxygen_generator_rating, "1", False) * solve(CO2_scrubber_rating, "0", True))
