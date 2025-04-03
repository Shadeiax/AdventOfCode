reports = []
reports_no_tol = []

with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        reports.append(list(map(int, line.strip().split())))


save_count = 0

def check_report(rep):
    direction = None
    for i in range(len(rep) - 1):
        diff = rep[i] - rep[i + 1]
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
        save_count += 1
    else:
        for j in range(len(report)):
            copy = report.copy()
            copy.pop(j)
            if check_report(copy):
                save_count += 1
                break

print(save_count)
