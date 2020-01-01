duels = int(input())

for duel in range(duels):
    percentages = [int(x) / 100 for x in input().split()]
    remaining = 100
    i = 0
    alan_chance = 0
    bob_chance = 0
    while remaining >= 0.1:
        if i % 2 == 0:
            this_shot = remaining * percentages[0]
            alan_chance += this_shot
            remaining -= this_shot
            i += 1
        if i % 2 == 1:
            this_shot = remaining * percentages[1]
            bob_chance += this_shot
            remaining -= this_shot
            i += 1
    print(round(alan_chance), " ")