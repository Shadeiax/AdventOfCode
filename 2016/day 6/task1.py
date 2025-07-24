from collections import Counter

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

message = ""
for index in range(len(input[0])):
    pos = [x[index] for x in input]
    message += Counter(pos).most_common()[0][0]

print(message)