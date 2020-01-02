winning_positions = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]

counter = int(input())

def win_checker(player):
    for position in winning_positions:
        if all(elem in player for elem in position):
            return True
    return False

for i in range(counter):
    x, y = [], []
    moves = input().split()
    current_turn = 1
    for move in moves:
        if current_turn % 2 == 1:
            x.append(move)
            if win_checker(x):
                print(str(current_turn) + " ")
                break
            current_turn += 1
        elif current_turn % 2 == 0:
            y.append(move)
            if win_checker(y):
                print(str(current_turn) + " ")
                break
            current_turn += 1
        if current_turn == 10:
            print("0 ")




