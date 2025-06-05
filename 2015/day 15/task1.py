mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)]

ingredients = []
for line in input:
    line = line.split()
    name = line[0][:-1]
    capacity = int(line[2][:-1])
    durability = int(line[4][:-1])
    flavor = int(line[6][:-1])
    texture = int(line[8][:-1])
    calories = int(line[10])
    ingredients.append(
        {"name": name, "capacity": capacity, "durability": durability, "flavor": flavor, "texture": texture, "calories": calories})

recipes = [(w, x, y, 100-w-x-y) for w in range(101) for x in range(101-w) for y in range(101-w-x) if w+x+y <= 100]
print(recipes)
print(ingredients)

res = 0
best_recipe = ()
for recipe in recipes:
    score = 0
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0

    for x in range(len(recipe)):
        capacity += ingredients[x]["capacity"] * recipe[x]
        durability += ingredients[x]["durability"] * recipe[x]
        flavor += ingredients[x]["flavor"] * recipe[x]
        texture += ingredients[x]["texture"] * recipe[x]

    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0

    score = capacity*durability*flavor*texture

    if score > res:
        res = score
        best_recipe = recipe

print(res)
print(best_recipe)
