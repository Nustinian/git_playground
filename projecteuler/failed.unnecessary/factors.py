from math import sqrt

def prime_factorize(number):
  factors = []
  if number == 0:
    return [0]
  while number % 2 == 0:
    number = number // 2
    factors.append(2)
  i = 3
  limit = int(sqrt(number))
  while number > 1 and i <= limit:
    if number % i == 0:
      factors.append(i)
      number = number // i
      limit = int(sqrt(number))
      if i > limit:
        factors.append(number)
    else:
      i += 2
      if i > limit:
        factors.append(number)
  return factors
