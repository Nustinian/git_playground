import math
counter = int(input())
for i in range(counter):
    a, b, c = [int(x) for x in input().split()]
    try:
        x1 = str(int((-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a))) + " "
        x2 = str(int((-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)))
    except ValueError:
        num = int(-b / (2 * a))
        complex = str(int(math.sqrt(abs(b**2 - 4 * a * c)) / (2 * a)))
        x1 = str(num) + "+" + complex + "i "
        x2 = str(num) + "-" + complex + "i"
    if i < counter - 1:
        print(x1 + x2 + "; ")
    else:
        print(x1 + x2)
