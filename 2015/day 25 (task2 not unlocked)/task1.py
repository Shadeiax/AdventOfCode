mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


test = 4,2
res = 3083,2978

def coord_nr(coords):
    x,y = coords
    x_base = x * (x+1) // 2

    y_base = 0
    for index in range(y-1):
        y_base += x + index

    res = x_base + y_base
    return res

test = coord_nr(test)
res = coord_nr(res)

def calc_solution(n):
    first = 20151125
    if n == 0:
        return res
    else:
        for x in range(n-1):
            first = (first * 252533) % 33554393
        return first

test = calc_solution(test)
res = calc_solution(res)

print(test)
print(res)