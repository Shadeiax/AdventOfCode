mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip().split() for line in open(file)]

triangles = [[int(input[i + j][x]) for j in range(3)] for i in range(0, len(input), 3) for x in range(3)]

count = sum(
    1 for tri in triangles if tri[0] + tri[1] > tri[2] and tri[0] + tri[2] > tri[1] and tri[1] + tri[2] > tri[0])

print(count)
