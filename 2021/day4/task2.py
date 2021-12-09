f = open("input", "r")
lines = f.readlines()

class Bingo_Board:
    def __init__(self,id):
        self.board = []
        self.solved = []
        self.id = id

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
                self.board[self.board.index(row)][row.index(num_string)] = "X"

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
    new_board = Bingo_Board(len(boards))
    while counter < 5:
        new_board.add_line(lines[x])
        counter += 1
        x += 1
    counter = 0
    x += 1
    boards.append(new_board)


drawn_index = 0

while len(boards) > 0:
    number = drawn_numbers[drawn_index]
    finished_boards = []
    for board in boards:
        board.check_num(number)
    for board in boards:
        if board.check_bingo():
            print(board.id,"BINGO with last number", number,"and solution", board.add_unmarked()*int(number))
            finished_boards.append(board)
    for board in finished_boards:
        boards.remove(board)
    drawn_index += 1
