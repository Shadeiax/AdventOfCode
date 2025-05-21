mode = 2
if mode == 1:
    file = "example.txt"
    space = 7
    end = 6,6
elif mode == 2:
    file = "input.txt"
    space = 71
    end = 70,70
input = [line.strip() for line in open(file)]


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print("")

start = 0,0
array = []
for x in range(space):
    for y in range(space):
        array.append((x, y))


for line in input:
    line = line.split(",")
    x, y = int(line[0]), int(line[1])
    array.remove((x, y))



def find_next_step(path, array):
    path = path.copy()
    pos = path[-1]
    y, x = pos

    possible_steps = [step for step in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)] if
                      step in array and step not in path]

    if len(possible_steps) > 0:
        new_paths = []
        for step in possible_steps:
            temp = path.copy()
            temp.append(step)
            new_paths.append(temp)
        return new_paths
    else:
        return [path]


def visualize_path(path, array):
    grid = [[" " for _ in range(space)] for _ in range(space)]

    for x in range(space):
        for y in range(space):
            if (x,y) in path:
                grid[y][x] = "0"
            elif (x,y) in array:
                grid[y][x] = "X"


    print_grid(grid)


active_paths = [[start]]
finished_paths = []

x = 0
while True:
    x += 1
    # find new steps for each path and replace active paths with new paths
    all_new_paths = []
    for path in active_paths:
        new_paths = find_next_step(path, array)
        all_new_paths.extend(new_paths)

    active_paths = all_new_paths
    all_new_paths = []

    # all checks needed on all active paths after computing step
    for path in active_paths:
        # check if path reached end
        if path[-1] == end:
            finished_paths.append(path)
            active_paths.remove(path)
            continue

        # remove all stuck paths
        if len(path) < x:
            active_paths.remove(path)
            continue

    # check if all paths are finished
    if len(active_paths) == 0:
        break



print(*finished_paths, sep="\n")
print(min(len(path) for path in finished_paths))

for path in finished_paths:
    visualize_path(finished_paths[0], array)