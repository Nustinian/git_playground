from useful import factorial

def paths(x, y):
    return factorial(x + y) // (factorial(x) * factorial(x + y - x))

ways = paths(20, 20)

print(ways)