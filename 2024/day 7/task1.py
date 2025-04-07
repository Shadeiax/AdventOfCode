from itertools import product

values = []
numbers = []

with open("input.txt", "r") as file:
    for n, line in enumerate(file.readlines()):
        value, num = line.split(":")
        values.append(value.strip())
        numbers.append(num.strip())

numbers = [x.split(' ') for x in numbers]

# function that returns all possible combinations to fill x slots from a given list of numbers
def get_combinations(slots):
    operators = ['+', '*']
    combs = list(product(operators, repeat=slots))
    return combs
def check_row(value, numbers):
    gaps = len(numbers) - 1
    combs = get_combinations(gaps)
    for comb in combs:
        term = ""
        for i in range(len(numbers) - 1):
            if i == 0:
                term = eval(numbers[0] + comb[0] + numbers[1])
            else:
                term = eval(str(term) + comb[i] + numbers[i + 1])
        if term == int(value):
            return int(value)
    return 0

sum = 0
for i, value in enumerate(values):
    sum += check_row(value, numbers[i])
print(sum)
