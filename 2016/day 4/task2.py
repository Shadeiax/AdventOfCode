from collections import Counter

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]


def decrypt(name, ID):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    for i in range(len(name)):
        if name[i].isalpha():
            name = name[:i] + alphabet[(alphabet.index(name[i]) + ID) % 26] + name[i + 1:]
    return name


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
        decrypted_name = decrypt(name, int(ID))
        if decrypted_name.startswith("north"):
            print(f"{decrypted_name}: {ID}")

print(res)
