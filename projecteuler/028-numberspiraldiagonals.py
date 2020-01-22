def sum_diagonals(max_length):
  sum = 1
  for i in range(3, max_length + 1, 2):
    sum += 4 * i ** 2 - 6 * (i - 1)
  return sum

print(sum_diagonals(1001))
