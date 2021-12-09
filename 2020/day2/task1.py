f = open("input", "r")
lines = f.readlines()

def check_validity(min, max, char, password):
    count = 0
    for character in password:
        if character == char:
            count += 1
    return int(min) <= count <= int(max)

counter = 0
for line in lines:
    split = line.split(" ")
    min_var = split[0].split("-")[0]
    max_var = split[0].split("-")[1]
    char_var = split[1].replace(":", "")
    password_var = split[2].replace("\n", "")
    if check_validity(min_var, max_var, char_var, password_var):
        counter+=1

print(counter)

