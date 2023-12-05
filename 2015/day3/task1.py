x,y = 0,0
houses = []

with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        for o, step in enumerate(line): #^>v<
            if step == "^":
                y+=1
            elif step =="v":
                y-=1
            elif step ==">":
                x+=1
            elif step =="<":
                x-=1
            if (x,y) not in houses:
                houses.append((x,y))
print(len(houses))
