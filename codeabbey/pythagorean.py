counter = int(input())
for i in range(counter):
    sides = [int(x) for x in input().split()]
    a2_plus_b2 = sides[0] ** 2 + sides[1] ** 2
    c2 = sides[2] ** 2
    if a2_plus_b2 == c2:
        print("R ")
    elif a2_plus_b2 > c2:
    	print("A ")
    else:
    	print("O ")
