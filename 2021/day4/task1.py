f = open("input", "r")
lines = f.readlines()

class Bingo_Board:
    def __init__(self):
        self.board = []
        self.solved = []

    def show(self):
        for row in self.board:
            print(row)
        print("")

    def add_line(self, line):
        self.board.append(line.split())

    def check_num(self, num_string):
        for row in self.board:
            if num_string in row:
                self.solved.append((self.board.index(row), row.index(num_string)))

    def check_bingo(self):
        row = 0
        column = 0
        while row < 5:
            while column < 5:
                if (row, column) in self.solved:
                    column += 1
                    if column == 5:
                        return True
                else:
                    break
            column = 0
            row += 1

        while column < 5:
            while row < 5:
                if (row, column) in self.solved:
                    row += 1
                    if row == 5:
                        return True
                else:
                    break
            row = 0
            column += 1
        return False

    def add_unmarked(self):
        sum = 0
        for row in self.board:
            for num in row:
                if (self.board.index(row), row.index(num)) not in self.solved:
                    sum += int(num)
        return sum


drawn_numbers = lines[0].split(",")

x = 2
counter = 0
boards = []
while x < len(lines)-1:
    new_board = Bingo_Board()
    while counter < 5:
        new_board.add_line(lines[x])
        counter += 1
        x += 1
    counter = 0
    x += 1
    boards.append(new_board)

bingo = False
drawn_index = 0
while bingo == False and drawn_index < len(drawn_numbers)-1:
    number = drawn_numbers[drawn_index]
    for board in boards:
        board.check_num(number)
        if board.check_bingo():
            bingo = True
            winning_board = board
            last_number = int(number)
            break
    drawn_index += 1

print(last_number)
print(winning_board.add_unmarked()*last_number)
