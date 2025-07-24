import hashlib

mode = 2
if mode == 1:
    door_id = "abc"
elif mode == 2:
    door_id = "abbhdwsy"

password = ""
index = 0
while len(password) < 8:
    hash_input = (door_id + str(index)).encode('utf-8')
    hash_result = hashlib.md5(hash_input).hexdigest()
    if hash_result.startswith('00000'):
        password += hash_result[5]
    index += 1

print(f"The password is: {password}")
