import re
from itertools import permutations

boss_data = "boss.txt"
shop = "shop.txt"

boss = [line.split(" ")[-1].strip() for line in open(boss_data)]
boss = [int(value) for value in boss]
input = [line.strip() for line in open(shop)]

mode = "weapons"
weapons = []
armors = []
rings = []

for line in input:
    if line == "":
        if mode == "weapons":
            mode = "armors"
            continue
        elif mode == "armors":
            mode = "rings"
            continue
    else:
        line = re.sub(r'\s+', " ", line)
        if mode == "weapons":
            weapons.append(line.split(" "))
        elif mode == "armors":
            armors.append(line.split(" "))
        elif mode == "rings":
            rings.append(line.split(" "))

for item in [weapons, armors, rings]:
    item.pop(0)
for item in rings:
    item[0] = item[0] + item[1]
    item.pop(1)

armors.append(["No Armor", 0, 0, 0])
rings.append(["No Ring", 0, 0, 0])

item_combs = []
items = []
for weapon in weapons:
    items.append(weapon)
    for armor in armors:
        items.append(armor)
        for combination in permutations(rings, 2):
            for ring in combination:
                items.append(ring)
            item_combs.append(items.copy())
            for ring in combination:
                items.remove(ring)
        items.remove(armor)
    items.remove(weapon)

print(len(item_combs))

def sim_fight(player, boss):
    player_hp, player_attack, player_armor, cost = player
    boss_hp, boss_attack, boss_armor = boss

    turn = 0
    while player_hp > 0 and boss_hp > 0:
        if turn == 0:
            boss_hp -= max(1, player_attack - boss_armor)
        elif turn == 1:
            player_hp -= max(1, boss_attack - player_armor)

        turn = int(not turn)

    if player_hp <= 0:
        return False
    else:  # boss_hp <= 0
        return True


max_cost = None
for comb in item_combs:
    player = [100, sum(int(item[2]) for item in comb), sum(int(item[3]) for item in comb),
              sum(int(item[1]) for item in comb)]
    if not sim_fight(player, boss):
        if max_cost:
            max_cost = max(max_cost, player[3])
        else:
            max_cost = player[3]
print(max_cost)
