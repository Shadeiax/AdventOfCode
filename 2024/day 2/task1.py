reports = []

with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        reports.append(list(map(int, line.strip().split())))

safe_count = int()

def check_report(rep):
    direction = None
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if diff > 0:
            curr_direction = "up"
        elif diff < 0:
            curr_direction = "down"
        else:
            return False
        if direction is None:
            direction = curr_direction
        elif direction != curr_direction:
            return False
        if diff == 0 or abs(diff) > 3:
            return False
    return True
for report in reports:
    if check_report(report):
        safe_count += 1


print(safe_count)