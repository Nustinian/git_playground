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
  if i > limit:
    factors.append(number)
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

def prod_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

primes = []
for i in range(20, 1, -1):
    factors = prime_factorize(i)
    for factor in factors:
        while primes.count(factor) < factors.count(factor):
            primes.append(factor)
print(prod_list(primes))