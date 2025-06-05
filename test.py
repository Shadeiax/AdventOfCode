recipes = [(w, x, y, 100-w-x-y) for w in range(101) for x in range(101-w) for y in range(101-w-x) if w+x+y <= 100]




print(recipes)