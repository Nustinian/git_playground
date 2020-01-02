import math

trees = int(input())
for tree in range(trees):
    values = [float(x) for x in input().split()]
    degrees = math.radians(values[1] - 90)
    height = round(math.tan(degrees) * values[0])
    print(height, " ")