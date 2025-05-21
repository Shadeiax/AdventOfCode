mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [[char for char in line.strip()] for line in open(file)]


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print("")


def find_next_step(path, grid):
    path = path.copy()
    pos = path[-1]
    y, x = pos

    possible_steps = [step for step in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)] if
                      grid[step[0]][step[1]] == "." and step not in path]

    if len(possible_steps) > 0:
        new_paths = []
        for step in possible_steps:
            temp = path.copy()
            temp.append(step)
            new_paths.append(temp)
        return new_paths
    else:
        return [path]


for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "S":
            start = (y, x)
        elif char == "E":
            end = (y, x)
            input[y][x] = "."


def visualize_path(path, grid):
    gridc = grid.copy()
    for step in path:
        y, x = step
        gridc[y][x] = "X"
    print_grid(gridc)


def calc_path_weight(path):
    direction_changes = 0

    for i in range(1, len(path)):
        curr_y, curr_x = path[i]
        prev_y, prev_x = path[i - 1]

        # Check direction change
        if i > 1:
            prev_prev_y, prev_prev_x = path[i - 2]
            prev_direction = (prev_y - prev_prev_y, prev_x - prev_prev_x)
            curr_direction = (curr_y - prev_y, curr_x - prev_x)
            if prev_direction != curr_direction:
                direction_changes += 1

    weight = len(path) - 1 + 1000 * (direction_changes + 1)
    return weight


direction = "right"
active_paths = [[start]]
finished_paths = []

x = 0
while True:
    x += 1
    print(x)
    # find new steps for each path and replace active paths with new paths
    all_new_paths = []
    for path in active_paths:
        new_paths = find_next_step(path, input)
        all_new_paths.extend(new_paths)

    active_paths = all_new_paths
    all_new_paths = []

    # all checks needed on all active paths after computing step
    for path in active_paths:
        # check if path isnt the shortest
        if len(finished_paths) > 0:
            if calc_path_weight(path) > min(calc_path_weight(path) for path in finished_paths):
                active_paths.remove(path)
                continue

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
print(min(calc_path_weight(path) for path in finished_paths))
