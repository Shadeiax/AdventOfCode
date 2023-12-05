rib = 0
with open("input", "r") as file:
    for n, package in enumerate(file.readlines()):
        x = package.strip().split("x")
        l, w, h = sorted((int(x[0]), int(x[1]), int(x[2])))
        rib += 2 * l + 2 * w + (l * w * h)
print(rib)
