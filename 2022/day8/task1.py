f = open("input", "r")
lines = f.readlines()

trees = []
for line in lines:
    hor = []
    for tree in line.strip():
        hor.append(int(tree))
    trees.append(hor)

visible = 0

for y in range(0, len(trees)):
    for x in range(0, len(trees)):
        vis_xpos = True
        vis_ypos = True
        vis_xneg = True
        vis_yneg = True
        for x_dec in range(x-1, -1, -1):
            if trees[y][x] <= trees[y][x_dec]:
                vis_xneg = False
        for y_dec in range(y-1, -1, -1):
            if trees[y][x] <= trees[y_dec][x]:
                vis_yneg = False
        for x_inc in range(x+1, len(trees)):
            if trees[y][x] <= trees[y][x_inc]:
                vis_xpos = False
        for y_inc in range(y+1, len(trees)):
            if trees[y][x] <= trees[y_inc][x]:
                vis_ypos = False
        if vis_xpos or vis_ypos or vis_xneg or vis_yneg:
            visible += 1

print(visible)
