from math import sqrt

def gpf(number):
  factors = []
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

def recursive_digit_changer(i, current):
  if current == 0:
    return current
  else:
    current[i], current[-i] == 1

 

def generate_palindromes(digits):
  listed_palindromes = []
  current = []
  for i in range(digits):
    current.append(0)
  listed_palindromes.append(current)
  if digits % 2 == 0:
    for 
  str_palindromes = ["".join(str(x) for x in palindrome) for palindrome in listed_palindromes]
  return str_palindromes
print(generate_palindromes(3))
palindromes = generate_palindromes(3)
