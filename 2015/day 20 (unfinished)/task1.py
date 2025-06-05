packages = 0
house = 680000
while True:
    for number in range(1, house+1):
        if house % number == 0:
            packages += number * 10
    house += 1
    if packages >= 29000000:
        print(house)
        break
    else:
        packages = 0

#3000 too low
#702240 too high