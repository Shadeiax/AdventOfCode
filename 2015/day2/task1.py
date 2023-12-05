res = 0
with open("input", "r") as file:
    for n, package in enumerate(file.readlines()):
        l, w, h = package.strip().split("x")
        res += 2 * int(l) * int(w) + 2 * int(w) * int(h) + 2 * int(h) * int(l) + min(int(l) * int(w), int(w) * int(h), int(h) * int(l))
print(res)
