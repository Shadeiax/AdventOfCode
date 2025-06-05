mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]
res = input[0]


def split_repeating_chars(s):
    result = []
    current_char = s[0]
    current_count = 1
    for char in s[1:]:
        if char == current_char:
            current_count += 1
        else:
            result.append((current_char, current_count))
            current_char = char
            current_count = 1
    result.append((current_char, current_count))
    result = ''.join(str(group[1]) + str(group[0]) for group in result)
    return result

for x in range(50):
    res = split_repeating_chars(res)

print(len(res))



