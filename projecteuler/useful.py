from math import sqrt
from functools import reduce

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

def generate_number_of_primes(limit):
  primes = []
  composites = {}
  current_number = 2
  while len(primes) < limit:
    if current_number not in composites:
      primes.append(current_number)
      composites[current_number ** 2] = [current_number]
    else:
      for factor in composites[current_number]:
        composites.setdefault(current_number + factor, []).append(factor)
      del composites[current_number]
    current_number += 1
  return primes

def generate_primes_up_to(limit):
  primes = []
  composites = {}
  current_number = 2
  while current_number < limit:
    if current_number not in composites:
      primes.append(current_number)
      composites[current_number ** 2] = [current_number]
    else:
      for factor in composites[current_number]:
        composites.setdefault(current_number + factor, []).append(factor)
      del composites[current_number]
    current_number += 1
  return primes

def factorial(x):
    if x == 0:
      return 0
    if x == 1:
        return 1
    return x * factorial(x - 1)

def get_all_factors(x):
  return list(set(reduce(list.__add__, ([i, x // i] for i in range(1, int(x ** 0.5) + 1) if x % i == 0))))
