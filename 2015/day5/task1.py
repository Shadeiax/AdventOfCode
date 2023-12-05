nice = 0
strings  = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]
with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        naughty = False
        vowel = 0
        double = False
        for o in strings :
            if o in line:
                naughty = True
        for p, letter in enumerate(line):
            if letter in vowels:
                vowel += 1
            if p < len(line)-1:
                if letter == line[p+1]:
                    double = True
        if not naughty and vowel >= 3 and double:
            nice += 1
print(nice)
