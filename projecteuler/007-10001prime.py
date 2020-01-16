def generate_primes(limit):
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

ten = generate_primes(10001)
print(ten[-1])
