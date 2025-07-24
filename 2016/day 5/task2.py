import hashlib

mode = 2
if mode == 1:
    door_id = "abc"
elif mode == 2:
    door_id = "abbhdwsy"

password = list("________")
index = 0
while password.count("_") > 0:
    hash_input = (door_id + str(index)).encode('utf-8')
    hash_result = hashlib.md5(hash_input).hexdigest()
    if hash_result.startswith('00000') and hash_result[5] in "01234567" and password[int(hash_result[5])] == "_":
        password[int(hash_result[5])] = hash_result[6]
        print(password)
    index += 1

password = "".join(password)
print(f"The password is: {password}")
