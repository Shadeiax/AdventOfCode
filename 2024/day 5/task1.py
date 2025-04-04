input = [line.strip() for line in open("input.txt")]
print(input)

separator_index = input.index('')
rules, updates = input[:separator_index], input[separator_index + 1:]


def check_update(update, rulelist):
    for rule in rulelist:
        if rule.split("|")[0] in update and rule.split("|")[1] in update:
            if update.index(rule.split("|")[0]) > update.index(rule.split("|")[1]):
                return False
    return True


sum = 0
for update in updates:
    if check_update(update, rules):
        sum += int(update.split(",")[len(update.split(",")) // 2])

print(sum)
