def parseInput():
    f = open("example", "r")
    lines = f.readlines()
    for i, l in enumerate(lines):
        lines[i] = l.strip().split(" -> ")
    for i1, pair in enumerate(lines):
        for i2, part in enumerate(pair):
            pair[i2] = (int(part.split(",")[0]), int(part.split(",")[1]))

    return lines

def fillTouples(touple_List):
    touples = []
    for pair in touple_List:
        if pair[0][0] == pair[1][0]:
            x = pair[0][0]
            if pair[0][1] > pair[1][1]:
                y = pair[1][1]
                while y <= pair[0][1]:
                    touples.append((x, y))
                    y += 1
            else:
                y = pair[0][1]
                while y <= pair[1][1]:
                    touples.append((x, y))
                    y += 1

        elif pair[0][1] == pair[1][1]:
            y = pair[0][1]
            if pair[0][0] > pair[1][0]:
                x = pair[1][0]
                while x <= pair[0][0]:
                    touples.append((x, y))
                    x += 1
            else:
                x = pair[0][0]
                while x <= pair[1][0]:
                    touples.append((x, y))
                    x += 1

    return touples


def fillGrid(input):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for touple in input:
        grid[touple[1]][touple[0]] += 1
    return grid

def countSpots(grid):
    counter = 0
    for row in grid:
        for spot in row:
            if spot > 1:
                counter += 1
    return counter



if __name__ == '__main__':
    input = parseInput()
    coordinates = fillTouples(input)
    grid = fillGrid(coordinates)
    print(countSpots(grid))


