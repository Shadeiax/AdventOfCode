from itertools import permutations

mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

towels = [towel.strip() for towel in input[0].split(",")]
patterns = [pattern for pattern in input[2:]]


#create a function that checks if a given string can be made from concatenating the strings in towels
def can_form_string(towels, pattern):
    for substring_length in range(len(pattern), 0, -1):
        for i in range(len(pattern) - substring_length + 1):
            substring = pattern[i:i + substring_length]
            if substring in towels:
                pattern = pattern[:i] + pattern[i + substring_length:]
                break
        else:
            return False


res = 0
for pattern in patterns:
    if can_form_string(towels, pattern):
        res += 1

print(res)