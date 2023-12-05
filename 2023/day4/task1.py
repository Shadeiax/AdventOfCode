total = 0
with open("input", "r") as file:
    for n, card in enumerate(file.readlines()):
        win_nums = card.strip().split(":")[1].split("|")[0].split()
        card_nums = card.strip().split(":")[1].split("|")[1].split()
        points = 0
        for num in card_nums:
            if num in win_nums:
                if points == 0:
                    points = 1
                else:
                    points*=2
        total+=points
        points=0
print(total)
