from useful import generate_primes_up_to as gp

primes = gp(1000000)

def add_digits(num):
  new_primes = []
  for digit in ['1', '3', '7', '9']:
    if int(num + digit) in primes:
      new_primes.append(num + digit)
  return new_primes

def from_left(num):
  while True:
    if int(num[1:]) not in primes:
      return False
    num = num[1:]
    if int(num) < 10:
      return True

myprimes = []

def recurse(num):
  if len(add_digits(num)) == 0:
    return
  else:
    for new_prime in add_digits(num):
      myprimes.append(new_prime)
      recurse(new_prime) 

for num in ['2', '3', '5', '7']:
  recurse(num)

sum = 0

for prime in myprimes:
  if from_left(prime):
    sum += int(prime)

print(sum)
