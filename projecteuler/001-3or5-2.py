def sum_multiples(number, limit):
  return number * (limit // number) * (1 + limit // number) / 2

print(sum_multiples(3, 999) + sum_multiples(5, 999) - sum_multiples(15, 999))