mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]
input = input[0]


def reformat(input):
    new = []
    for i, x in enumerate(input):
        # if x == file
        if i % 2 == 0:
            for x in range(int(x)):
                new.append(str(int(i) // 2))
        # if x == free space
        else:
            for x in range(int(x)):
                new.append(".")
    return new


def new_compact(input):
    return input


def checksum(input):
    checksum = 0
    for i, x in enumerate(input):
        if x != ".":
            checksum += int(x) * i
    return checksum


def listprint(list):
    for i in range(len(list)):
        print(list[i], end="")
    print()


res = reformat(input)
listprint(res)
res = new_compact(res)
listprint(res)
print(checksum(res))
