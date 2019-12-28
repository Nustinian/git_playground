counter = int(input())
for i in range(counter):
    games = input().split()
    player_one_points = 0
    player_two_points = 0
    for game in games:
        if game[0] == game[1]:
            continue
        if game[0] == "R" and game[1] == "S":
            player_one_points += 1
        elif game[0] == "P" and game[1] == "R":
            player_one_points += 1
        elif game[0] == "S" and game[1] == "P":
            player_one_points += 1
        else:
            player_two_points += 1
    if player_one_points > player_two_points:
        print("1 ")
    else:
        print("2 ")

