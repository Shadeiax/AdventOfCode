def full_dict():
    dict = {}
    for x in range(9):
        dict[x] = 0
    return dict

if __name__ == '__main__':
    f = open("input", "r")
    lines = f.readlines()
    fish = [int(x) for x in lines[0].split(",")]

    X = full_dict()
    for f in fish:
        X[f] += 1
    print(X)

    for day in range(256):
        Y = full_dict()
        for x, amount in X.items():
            if x == 0:
                Y[6] += amount
                Y[8] += amount
            else:
                Y[(x - 1)] += amount
        X = Y

    print(sum(X.values()))
