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

def intify(list_number):
    return int("".join(list_number))

def generate_palindromes(list_number, i = 0):
    if len(list_number) % 2 == 0:
        must_change = len(list_number) // 2
    else:
        must_change = len(list_number) // 2 + 1    
    changed_nums = []
    for j in range(10):
        new_list = list_number[:]
        new_list[i], new_list[-1 - i] = str(j), str(j)
        changed_nums.append((new_list))
        if i != must_change:
            changed_nums += generate_palindromes(new_list, i + 1)
    palindromes = []
    for num in changed_nums:
        if num not in palindromes:
            palindromes.append(num)
    return palindromes

number = ["0", "0", "0", "0", "0", "0"]
cake = [prime_factorize(intify(x)) for x in generate_palindromes(number)]



