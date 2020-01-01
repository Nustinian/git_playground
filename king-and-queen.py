counter = int(input())
for i in range(counter):
    king, queen = input().split()
    horizontal_distance = abs(ord(king[0]) - ord(queen[0]))
    vertical_distance = abs(int(king[1]) - int(queen[1]))
    if horizontal_distance == vertical_distance:
        print("Y ")
    elif king[0] == queen[0] or king[1] == queen[1]:
        print("Y ")
    else:
        print("N ")