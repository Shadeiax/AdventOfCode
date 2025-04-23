mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]
input = input[0]


def reformat(input):
    new: String = ""
    for i, x in enumerate(input):
        # if x == file
        if i % 2 == 0:
            for x in range(int(x)):
                new += str(int(i) // 2)
        # if x == free space
        else:
            for x in range(int(x)):
                new += "."
    return new


def compact(input):
    new = [char for char in input]
    # swap last data with first free space
    for ind in range(len(new) - 1, 0, -1):
        if new[ind] != ".":
            ind2 = new.index(".")
            new[ind], new[ind2] = new[ind2], new[ind]
        # check if sorted
        dots = [i for i, n in enumerate(new) if n == "."]
        if dots[len(dots) - 1] == len(new) - 1 and dots[len(dots) - 1] - dots[0] == len(dots) - 1:
            return "".join(new)


def new_compact(input):
    nums = [i for i in input if i.isdigit()]
    inds = [i for i in range(len(input)) if input[i] == "."]
    new = [char for char in input]
    for i in range(len(inds)):
        new[inds[i]] = nums[len(nums) - 1 - i]
    for i in range(len(inds)):
        pass
        #new.pop()
    return "".join(new)


def checksum(input):
    new = [char for char in input]
    checksum = 0
    for i, x in enumerate(new):
        if x != ".":
            checksum += int(x) * i
    return checksum


res = reformat(input)
print(res+"\n")
res = new_compact(res)
print(res+"\n")
print(checksum(res))
