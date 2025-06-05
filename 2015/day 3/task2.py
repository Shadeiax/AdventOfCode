x1,y1 = 0,0
x2,y2 = 0,0
houses = [(0,0)]

with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        for o, step in enumerate(line): #^>v<
            if o % 2 == 0:
                if step == "^":
                    y1+=1
                elif step =="v":
                    y1-=1
                elif step ==">":
                    x1+=1
                elif step =="<":
                    x1-=1
                if (x1,y1) not in houses:
                    houses.append((x1,y1))
            elif o % 2 == 1:
                if step == "^":
                    y2+=1
                elif step =="v":
                    y2-=1
                elif step ==">":
                    x2+=1
                elif step =="<":
                    x2-=1
                if (x2,y2) not in houses:
                    houses.append((x2,y2))
print(len(houses))
