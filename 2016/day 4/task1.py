from collections import Counter

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

res = 0
for crypt in input:
    name, rest = crypt.rsplit("-", 1)
    ID, checksum = rest.split('[', maxsplit=1)
    checksum = [l for l in checksum[:-1]]

    # Count letters in name
    letter_counts = Counter(c for c in name if c.isalpha())
    sorted_counts = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    top_five = [letter for letter, count in sorted_counts[:5]]

    if top_five == checksum:
        res += int(ID)

print(res)
