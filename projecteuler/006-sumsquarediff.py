def sum_up_to(limit):
    return limit * (limit + 1) // 2

def sum_squares_to(limit):
    return sum([x ** 2 for x in range(limit + 1)])

def sum_square_diff(limit):
    return sum_up_to(limit) ** 2 - sum_squares_to(limit)

print(sum_square_diff(100))