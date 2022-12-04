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
    print(line)

    if line[1] == "X":
        if line[0] == "A":
            ur_choice = "Z"
        elif line[0] == "B":
            ur_choice = "X"
        elif line[0] == "C":
            ur_choice = "Y"
    elif line[1] == "Y":
        score += 3
        ur_choice = line[0]
    elif line[1] == "Z":
        score += 6
        if line[0] == "A":
            ur_choice = "Y"
        elif line[0] == "B":
            ur_choice = "Z"
        elif line[0] == "C":
            ur_choice = "X"

    score += choice.get(ur_choice)

print(score)

