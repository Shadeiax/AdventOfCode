with open("input", "r") as file:
    lines = file.readlines()
    cards = [1 for _ in range(len(lines))]
    for n, card in enumerate(lines):
        win_nums = card.strip().split(":")[1].split("|")[0].split()
        card_nums = card.strip().split(":")[1].split("|")[1].split()
        matches = 0
        for num in card_nums:
            if num in win_nums:
                matches+=1
        for var in range(1,matches+1):
            if n+var < len(cards):
                cards[n+var] += cards[n]
        matches = 0
print(sum(cards))
