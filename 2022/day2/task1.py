f = open("input", "r")
lines = f.readlines()

choice = {"A": 1,
          "B": 2,
          "C": 3,
          "X": 1,
          "Y": 2,
          "Z": 3
          }

score = 0
for line in lines:
    line = line.split()
    score += choice.get(line[1])

    if line[0] == "A" and line[1] == "Y":
        score += 6
    elif line[0] == "B" and line[1] == "Z":
        score += 6
    elif line[0] == "C" and line[1] == "X":
        score += 6

    elif choice.get(line[1]) == choice.get(line[0]):
        score += 3

    print(choice.get(line[0]), choice.get(line[1]))

print(score)

