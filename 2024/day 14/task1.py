mode = 2
if mode == 1:
    file = "example.txt"  #
    width = 11
    height = 7
elif mode == 2:
    file = "input.txt"
    width = 101
    height = 103
input = [line.strip() for line in open(file)]


class Robot:
    def __init__(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.quadrant = self.check_quadrant()

    def move(self):
        for x in range(100):
            self.x += self.x_velocity
            self.y += self.y_velocity
            if self.x < 0:
                self.x += width
            if self.x > width - 1:
                self.x -= width
            if self.y < 0:
                self.y += height
            if self.y > height - 1:
                self.y -= height
        self.quadrant = self.check_quadrant()

    def check_quadrant(self):
        if self.x > (width // 2) and self.y > (height // 2):
            return 1
        elif self.x < (width // 2) and self.y > (height // 2):
            return 2
        elif self.x < (width // 2) and self.y < (height // 2):
            return 3
        elif self.x > (width // 2) and self.y < (height // 2):
            return 4
        else:
            return 0


robots = []
for line in input:
    split = (line.split()[0][2:].split(",")[0], line.split()[0][2:].split(",")[1],
             line.split()[1][2:].split(",")[0], line.split()[1][2:].split(",")[1])
    robots.append(Robot(int(split[0]), int(split[1]), int(split[2]), int(split[3])))

for robot in robots:
    robot.move()

quadrants = [robot.quadrant for robot in robots]
print(quadrants)
safety_factor = quadrants.count(1) * quadrants.count(2) * quadrants.count(3) * quadrants.count(4)
print(safety_factor)

vis = [["." for _ in range(width)] for _ in range(height)]
for robot in robots:
    if vis[robot.y][robot.x] == ".":
        vis[robot.y][robot.x] = 1
    else:
        vis[robot.y][robot.x] += 1
vis = ["".join(map(str, row)) for row in vis]
print(*vis, sep="\n")
