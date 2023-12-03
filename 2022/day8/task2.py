f = open("example", "r")
lines = f.readlines()

trees = []
for line in lines:
    hor = []
    for tree in line.strip():
        hor.append(int(tree))
    trees.append(hor)
max = 0
for y in range(1, len(trees)-1):
    for x in range(1, len(trees)-1):
        vis_xpos = 0
        vis_ypos = 0
        vis_xneg = 0
        vis_yneg = 0
        for x_dec in range(x-1, -1, -1):
            if trees[y][x] > trees[y][x_dec]:
                vis_xneg += 1
            elif trees[y][x] == trees[y][x_dec]:
                vis_xneg += 1
                break
            else:
                break
        for y_dec in range(y-1, -1, -1):
            if trees[y][x] > trees[y_dec][x]:
                vis_yneg += 1
            elif trees[y][x] == trees[y_dec][x]:
                vis_yneg += 1
                break
            else:
                break
        for x_inc in range(x+1, len(trees)):
            if trees[y][x] > trees[y][x_inc]:
                vis_xpos += 1
            elif trees[y][x] == trees[y][x_inc]:
                vis_xpos += 1
                break
            else:
                break
        for y_inc in range(y+1, len(trees)):
            if trees[y][x] > trees[y_inc][x]:
                vis_ypos += 1
            elif trees[y][x] == trees[y_inc][x]:
                vis_ypos += 1
                break
            else:
                break
        print(vis_yneg,vis_xneg,vis_ypos,vis_xpos)
        value = vis_yneg*vis_xneg*vis_ypos*vis_xpos
        if value > max:
            max = value


print(max)

