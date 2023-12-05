nice = 0

with open("example", "r") as file:
    for n, line in enumerate(file.readlines()):
        pairs = []
        pair = False
        rep = False
        for o, letter in enumerate(line.strip()):
            if o < len(line) - 2:
                if letter == line[o + 2]:
                    rep = True
            if o > 0:
                pairs.append((line[o - 1] + letter).strip())

        print(pairs)
        for pair in pairs:
            if pairs.count(pair) > 1:
                print(pair)
                pair = True
        if rep and pair:
            nice += 1
print(nice)
