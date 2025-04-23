x = "00...................................151"

def new_compact(input):
    nums = [i for i in input if i.isdigit()]
    inds = [i for i in range(len(input)) if input[i] == "."]
    new = [char for char in input]
    for i in range(len(inds)):
        new[inds[i]] = nums[len(nums) - 1 - i]
    for i in range(len(inds)):
        new.pop()
    return "".join(new)

x = new_compact(x)
print(x)
