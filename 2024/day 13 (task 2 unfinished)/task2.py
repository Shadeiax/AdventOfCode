mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file) if line != "\n"]


class Claw:
    def __init__(self, a_x, a_y, b_x, b_y, end_x, end_y):
        self.valid_combinations = []
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.end_x = end_x
        self.end_y = end_y
        self.a_cost = 3
        self.b_cost = 1
        self.cost = int()

    def print(self):
        print("Button A: X+{}, Y+{}".format(self.a_x, self.a_y))
        print("Button B: X+{}, Y+{}".format(self.b_x, self.b_y))
        print("End: X+{}, Y+{}".format(self.end_x, self.end_y), end="\n\n")

    def get_possible_combinations(self):
        self.x_combinations = []
        for a in range((self.end_x // self.a_x) + 1):
            b = (self.end_x - (a * self.a_x)) / self.b_x
            c = (self.end_y - (a * self.a_y)) / self.b_y
            if b.is_integer() and b == c:
                self.valid_combinations.append((a, int(b), self.a_cost * a + self.b_cost * int(b)))

        self.valid_combinations.sort(key=lambda x: x[2])
        if len(self.valid_combinations) != 0:
            self.cost = self.valid_combinations[0][2]


claws = []
for i in range(len(input)):
    if i % 3 == 0:
        a_x, a_y = int(input[i].split()[2][1:-1]), int(input[i].split()[3][1:])
    elif i % 3 == 1:
        b_x, b_y = int(input[i].split()[2][1:-1]), int(input[i].split()[3][1:])
    elif i % 3 == 2:
        end_x, end_y = int(input[i].split()[1][2:-1])+10000000000000, int(input[i].split()[2][2:])+10000000000000
        claw = Claw(a_x, a_y, b_x, b_y, end_x, end_y)
        claws.append(claw)

for claw in claws:
    claw.get_possible_combinations()

print(sum(claw.cost for claw in claws))
