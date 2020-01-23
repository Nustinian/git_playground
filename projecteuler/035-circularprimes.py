from useful import generate_primes_up_to as gp
primes = gp(1000000)
primes_without_evens = [x for x in primes if not any(z in ['0', '2', '4', '5', '6', '8'] for z in str(x))]
def rotate(num, positions):
  return int(str(num)[positions:] + str(num)[:positions])

counter = 2

for prime in primes_without_evens:
  for i in range(len(str(prime))):
    if rotate(prime, i) not in primes:
      break
    if i == len(str(prime)) - 1:
      counter += 1

print(counter)
