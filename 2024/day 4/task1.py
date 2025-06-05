import numpy as np

array = []

def arr_print(arr):
    for l in arr:
        print(l)

with open("boss.txt", "r") as file:
    for n, line in enumerate(file.readlines()):
        line = [x for x in line.strip()]
        array.append(line)


array = np.array(array)

###vorwärts
#gerade
gerade = array.copy()
runter = array.copy().transpose()
diagonal = [array.diagonal(i).tolist() for i in range(-array.shape[0] + 1, array.shape[1])]
diagonal += [np.fliplr(array).diagonal(i).tolist() for i in range(-array.shape[0] + 1, array.shape[1])]

###reverse
gerade_r = [d[::-1] for d in gerade]
runter_r = [d[::-1] for d in runter]
diagonal_r = [d[::-1] for d in diagonal]

arrays = [gerade,gerade_r,runter,runter_r,diagonal,diagonal_r]

count = 0

def count_xmas(array):
    count = 0
    for entry in array:
        for i, x in enumerate(entry):
            if i < 3:
                continue
            elif len(entry) < 4:
                continue
            elif entry[i-3]+entry[i-2]+entry[i-1]+x == "XMAS":
                count += 1
    return count

count = 0

for arr in arrays:
    count += count_xmas(arr)

print(count)





