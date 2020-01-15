def get_prime_factors(number):
  i = 2
  while number > 1:
    if number % i == 0:
      largest_prime = i
      number = number / i
    else:
      i += 1
  return largest_prime

print(get_prime_factors(int(input())))