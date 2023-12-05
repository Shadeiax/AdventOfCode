with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        score = 0
        for o, c in enumerate(line):
            if c == "(":
                score += 1
            elif c == ")":
                score -= 1
            if score < 0:
                print(o+1)
                break
