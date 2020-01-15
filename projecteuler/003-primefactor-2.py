from math import sqrt

def get_prime_factors(number):
  largest_prime = 1
  if number % 2 == 0:
    number = number / 2
    largest_prime = 2
  i = 3
  limit = sqrt(number)
  while number > 1 and i < limit:
    if number % i == 0:
      largest_prime = i
      number = number / i
      limit = sqrt(number)
      if i > limit:
        largest_prime = number
    else:
      i += 2
  return largest_prime

print(get_prime_factors(int(input())))
