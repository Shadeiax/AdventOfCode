if __name__ == '__main__':
    f = open("input", "r")
    lines = f.readlines()
    fish = [int(x) for x in lines[0].split(",")]
    days = 256

    for d in range(days):
        for i,f in enumerate(fish):
            fish[i] -= 1
        for i, f in enumerate(fish):
            if fish[i] == -1:
                fish[i] = 6
                fish.append(8)

    print(len(fish))

