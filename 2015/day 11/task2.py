mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

curr_password = input[0]


def increment(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i] != "z":
            string[i] = chr(ord(string[i]) + 1)
            return "".join(string)
        else:
            string[i] = "a"
    return "".join(string)


def check(password):
    # Straight of three letters
    straight_found = False
    for i in range(len(password) - 3):
        if ord(password[i]) + 2 == ord(password[i + 1]) + 1 == ord(password[i + 2]):
            straight_found = True
            break
    if not straight_found:
        # print("no straight found")
        return False

    # no "i", "o" or "l"
    if "i" in password or "o" in password or "l" in password:
        # print("i, o or l")
        return False

    # Two pairs
    pairs = []
    for i in range(len(password) - 1):
        if i > 0:
            if password[i - 1] == password[i]:
                continue
        if password[i] == password[i + 1]:
            pairs.append(password[i])
    if len(pairs) < 2:
        # print("not enough pairs")
        return False

    return True

for x in range(2):
    while not check(curr_password):
        curr_password = increment(list(curr_password))
    if x == 0:
        curr_password = increment(list(curr_password))

print(curr_password)
