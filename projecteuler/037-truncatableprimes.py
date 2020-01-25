from useful import generate_primes_up_to as gp

primes = gp(1000000)

def from_left(prime):
  strnum = str(prime)
  while True:
    if int(strnum[1:]) not in primes:
      return False
    strnum = strnum[1:]
    if int(strnum) < 10:
      return True

def from_right(prime):
  strnum = str(prime)
  while True:
    if int(strnum[:-1]) not in primes:
      return False
    strnum = strnum[:-1]
    if int(strnum) < 10:
      return True

sum = 0
for prime in primes[4:]:
  if (prime < 10000 or prime > 100000) and (from_right(prime) and from_left(prime)):
    sum += prime

print(sum)


