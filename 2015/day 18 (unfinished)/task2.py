from itertools import product

offsets = list(product((0, -1, 1), repeat=2))
print(offsets)

coords = 2, 3
y, x = coords
for off in offsets:
    check = y + off[0], x + off[1]
    print(check)
