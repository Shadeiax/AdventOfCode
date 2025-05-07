mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

input = [i for i in input]


def find_letter_coordinates(matrix: list[list[str]]) -> list[tuple[str, list[tuple[int, int]]]]:
    regions = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            letter = matrix[y][x]
            regions.append((letter, [(y, x)]))
    return regions


def check_if_connected(region1, region2):
    for coord1 in region1[1]:
        for coord2 in region2[1]:
            if region1[0] == region2[0] and ((abs(coord1[0] - coord2[0]) == 1 and coord1[1] == coord2[1]) or
                                             (abs(coord1[1] - coord2[1]) == 1 and coord1[0] == coord2[0])):
                return True
    return False


def compact_regions(regions):
    # Group all regions where check if connected is True
    sorting = True
    while sorting:
        sorting = False
        for i in range(len(regions)):
            for j in range(i + 1, len(regions)):
                if check_if_connected(regions[i], regions[j]):
                    regions[i][1].extend(regions[j][1])
                    regions.pop(j)
                    sorting = True
                    break
    return regions


def find_letter_corners(regions):
    borders = []
    for letter, coords in regions:
        walls = []
        corners = []
        for coord in coords:
            x, y = coord
            for neighbour in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if neighbour not in coords:
                    if neighbour not in walls:
                        walls.append(neighbour)
                    else:
                        corners.append(neighbour)
        borders.append((letter, len(corners), len(coords)))
    return borders


coordinates = find_letter_coordinates(input)
print(*coordinates, sep="\n", end="\n------ regions\n")
coordinates = compact_regions(coordinates)
print(*coordinates, sep="\n", end="\n------ compacted regions\n")
borders = find_letter_corners(coordinates)
print(*borders, sep="\n", end="\n------ borders\n")

print("Total price:", sum([len(border[1]) for border in borders]))
