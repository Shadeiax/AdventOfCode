mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

def is_nice(string):
    repeating_pair = False
    repeating_letter = False

    #check for repeating pair
    for i in range(len(string) - 1):
        pair = string[i:i + 2]
        for j in range(i + 2, len(string) - 1):
            if pair == string[j:j + 2]:
                repeating_pair = True
                break
        if repeating_pair:
            break

    #check for repeating letter
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            repeating_letter = True
            break

    return repeating_letter and repeating_pair

res = 0
for line in input:
    print(line, is_nice(line))
    if is_nice(line):
        res += 1

print(res)