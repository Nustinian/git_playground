grid = []
with open("011-grid.txt") as file:
    line = file.readline()
    while line:
        grid.append([int(x) for x in line.strip('\n').split(' ')])
        line = file.readline()

def diagonal_right(x, y):
    return grid[y][x] * grid[y + 1][x + 1] * grid[y + 2][x + 2] * grid[y + 3][x + 3]

def diagonal_left(x, y):
    return grid[y][x] * grid[y + 1][x - 1] * grid[y + 2][x - 2] * grid[y + 3][x - 3]

def vertical_product(x, y):
    return grid[y][x] * grid[y + 1][x] * grid[y + 2][x] * grid[y + 3][x]

def horizontal_product(x, y):
    return grid[y][x] * grid[y][x + 1] * grid[y][x + 2] * grid[y][x + 3]

def all_three(x, y):
    return max(diagonal_right(x, y), vertical_product(x, y), horizontal_product(x, y))

highest_product = 0
for y in range(20):
    if y <= 16:
        for x in range(20):
            if x <= 16:
                test = all_three(x, y)
                if test > highest_product:
                    highest_product = test
            else:
                test = vertical_product(x, y)
                if test > highest_product:
                    highest_product = test
            if x >= 3:
                test = diagonal_left(x, y)
                if test > highest_product:
                    highest_product = test
    else:
        for x in range(20):
            if x <= 16:
                test = horizontal_product(x, y)
                if test > highest_product:
                    highest_product = test

print(highest_product)