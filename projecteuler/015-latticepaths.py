paths_dict = {}

def paths(x, y):
    if (x, y) not in paths_dict:
        if x == 1:
            paths_dict[(x, y)] = y + 1
        elif y == 1:
            paths_dict[(x, y)] = x + 1
        else:
            paths_dict[(x, y)] = paths(x - 1, y) + paths(x, y - 1)
    return paths_dict[(x, y)]


print(paths(20, 20))
