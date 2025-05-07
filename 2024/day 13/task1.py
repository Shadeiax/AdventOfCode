mode = 1
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file) if line != "\n"]


class Claw:
    def __init__(self, a_x, a_y, b_x, b_y, end_x, end_y):
        self.valid_combinations = [(int(), int())]
        self.combinations = [(int(), int())]
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.end_x = end_x
        self.end_y = end_y
        self.a_cost = 3
        self.b_cost = 2

    def get_possible_combinations(self):
        self.x_combinations = []
        for a in range((self.end_x // self.a_x) + 1):
            b = (self.end_x - a * self.a_x) / self.b_x
            if b.is_integer():
                self.x_combinations.append((a, int(b)))

        self.y_combinations = []
        for a in range((self.end_y // self.a_y) + 1):
            b = (self.end_y - a * self.a_y) / self.b_y
            if b.is_integer():
                self.y_combinations.append((a, int(b)))

        print(self.x_combinations)
        print(self.y_combinations)


claws = []
for i in range(len(input)):
    if i % 3 == 0:
        a_x, a_y = int(input[i].split()[2][1:-1]), int(input[i].split()[3][1:-1])
    elif i % 3 == 1:
        b_x, b_y = int(input[i].split()[2][1:-1]), int(input[i].split()[3][1:-1])
    elif i % 3 == 2:
        end_x, end_y = int(input[i].split()[1][2:-1]), int(input[i].split()[2][2:-1])
        claw = Claw(a_x, a_y, b_x, b_y, end_x, end_y)
        claws.append(claw)

claws[0].get_possible_combinations()
