mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

input = [int(i) for i in input[0].split()]

print(input)


def blink(stones, blinks):
    for x in range(blinks):
        new = []
        for stone in stones:
            if stone == 0:
                new.append(1)
            elif len(str(stone)) % 2 == 0:
                l = len(str(stone)) // 2
                new.extend([int(str(stone)[:l]), int(str(stone)[l:])])
            else:
                new.append(stone * 2024)
        stones = new
    return stones

res = blink(input,75)
print(len(res))
