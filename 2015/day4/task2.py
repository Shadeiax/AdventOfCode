import hashlib

with open("input", "r") as file:
    input = file.readlines()[0]
    found = False
    i = 0
    while not found:
        result = hashlib.md5((input+str(i)).encode())
        if result.hexdigest()[0:6] == "000000":
            print(i)
            found = True
        i += 1