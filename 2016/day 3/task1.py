mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [[int(x) for x in line.strip().split()] for line in open(file)]

count = sum(
    1 for tri in input if tri[0] + tri[1] > tri[2] and tri[0] + tri[2] > tri[1] and tri[1] + tri[2] > tri[0])

print(count)
