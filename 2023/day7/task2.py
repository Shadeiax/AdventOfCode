cards = {"A": 14,
         "K": 13,
         "Q": 12,
         "T": 10,
         "9": 9,
         "8": 8,
         "7": 7,
         "6": 6,
         "5": 5,
         "4": 4,
         "3": 3,
         "2": 2,
         "J": 1}


def check_hand(shand):
    shand = sorted(shand)
    possibilities = []
    for i in range(1, 15):
        clone = shand.copy()
        for repl_in, card in enumerate(shand):
            if card == 1:
                clone[repl_in] = i
        clone = sorted(clone)
        print(clone)
        a, b, c, d, e = clone[0], clone[1], clone[2], clone[3], clone[4]
        # Five of a kind
        if a == b == c == d == e:
            possibilities.append(7)
        # Four of a kind
        elif a == b == c == d or b == c == d == e:
            possibilities.append(6)
        # Full House
        elif a == b == c and d == e or a == b and c == d == e:
            possibilities.append(5)
        # Three of a kind
        elif a == b == c or b == c == d or c == d == e:
            possibilities.append(4)
        # Two pairs
        elif a == b and c == d or a == b and d == e or b == c and d == e:
            possibilities.append(3)
        # One pair
        elif a == b or b == c or c == d or d == e:
            possibilities.append(2)
        # High card
        else:
           possibilities.append(1)
    return max(possibilities)

hands = []
with open("input", "r") as file:
    for n, line in enumerate(file.readlines()):
        hand, bid = line.strip().split(" ")
        hand = list(hand)
        for i, card in enumerate(hand):
            hand[i] = cards.get(card)
        first = hand[0]
        type = check_hand(hand)
        hands.append((hand, type, int(bid)))
    print(hands)

hands.sort(key=lambda x: (x[1], x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))

winnings = []
for i, hand in enumerate(hands):
    winnings.append(hand[2] * (i + 1))
print(sum(winnings))
