input = [line.strip() for line in open("input.txt")]


separator_index = input.index('')
rules, updates = input[:separator_index], [update.split(",") for update in input[separator_index + 1:]]

def check_update(update, rulelist):
    for rule in rulelist:
        if rule.split("|")[0] in update and rule.split("|")[1] in update:
            if update.index(rule.split("|")[0]) > update.index(rule.split("|")[1]):
                return False
    return True

def reorder_update(update, rulelist):
    correct = False
    while not correct:
        correct = True
        for rule in rulelist:
            l,r = rule.split("|")
            if l in update and r in update:
                l_i, r_i = update.index(l), update.index(r)
                if l_i > r_i:
                    correct = False
                    update[l_i], update[r_i] = update[r_i], update[l_i]
    return update


sum = 0
for update in updates:
    if not check_update(update, rules):
        update = reorder_update(update, rules)
        sum += int(update[len(update) // 2])

print(sum)
