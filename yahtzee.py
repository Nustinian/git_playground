def check_straights(dice):
    small_straight = ['1', '2', '3', '4', '5']
    if all(die in dice for die in small_straight):
        return True, "small-straight "
    big_straight = ['2', '3', '4', '5', '6']
    if all(die in dice for die in big_straight):
        return True, "big-straight "

def count(dice):
    counts = {}
    number, occurrences = '', 0
    for die in dice:
        counts[die] = counts.get(die, 0) + 1
        if counts[die] >= occurrences:
            number, occurrences = die, counts[die]
    for i in range(occurrences):
        dice.remove(number)
    counts2 = {}
    occurrences2 = 0
    for die in dice:
        counts2[die] = counts2.get(die, 0) + 1
        if counts2[die] >= occurrences2:
            occurrences2 = counts2[die]
    return occurrences, occurrences2


def determine_pairs(occurrences, occurrences2):
    if occurrences == 5:
        return "yacht "
    elif occurrences == 4:
        return "four "
    elif occurrences == 3:
        if occurrences2 == 2:
            return "full-house "
        else:
            return "three "
    elif occurrences == 2:
        if occurrences2 == 2:
            return "two-pairs "
        else:
            return "pair "
    elif occurrences == 1:
        return "none "

for i in range(int(input())):
    dice = input().split()
    if check_straights(dice):
        print(check_straights(dice)[1])
        continue
    occurrences, occurrences2 = count(dice)
    print(determine_pairs(occurrences, occurrences2))


