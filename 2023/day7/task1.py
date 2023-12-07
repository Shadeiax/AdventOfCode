cards = {"A": 14,
         "K": 13,
         "Q": 12,
         "J": 11,
         "T": 10,
         "9": 9,
         "8": 8,
         "7": 7,
         "6": 6,
         "5": 5,
         "4": 4,
         "3": 3,
         "2": 2}

def check_hand(shand):
    shand = sorted(shand)
    a, b, c, d, e = shand[0], shand[1], shand[2], shand[3], shand[4]
    # Five of a kind
    if a == b == c == d == e:
        return 7
    # Four of a kind
    if a == b == c == d or b == c == d == e:
        return 6
    # Full House
    if a == b == c and d == e or a == b and c == d == e:
        return 5
    # Three of a kind
    if a == b == c or b == c == d or c == d == e:
        return 4
    # Two pairs
    if a == b and c == d or a == b and d == e or b == c and d == e:
        return 3
    # One pair
    if a == b or b == c or c == d or d == e:
        return 2
    # High card
    return 1

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

hands.sort(key=lambda x: (x[1], x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))

winnings = []
for i, hand in enumerate(hands):
    winnings.append(hand[2] * (i + 1))
print(sum(winnings))
