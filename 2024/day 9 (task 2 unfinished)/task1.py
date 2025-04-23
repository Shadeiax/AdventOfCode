mode = 2
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
    nums = [i for i in input if i.isdigit()]
    inds = [i for i in range(len(input)) if input[i] == "."]
    new = [char for char in input]
    for i in range(len(inds)):
        new[inds[i]] = nums[len(nums) - 1 - i]
    for i in range(len(inds)):
        pass
        new.pop()
    return new


def checksum(input):
    checksum = 0
    for i, x in enumerate(input):
        if x != ".":
            checksum += int(x) * i
    return checksum


res = reformat(input)
print(res)
res = new_compact(res)
print(res)
print(checksum(res))
