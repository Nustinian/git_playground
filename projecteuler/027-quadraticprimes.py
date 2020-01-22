##solved in the interpreter

from useful import generate_primes_up_to as gp

primes = gp(5000)

def test_nums(x, y, n):
  output = []
  for i in range(n):
    output.append(i ** 2 + x * i + y)
  return output

## tested test_nums(1, 41, 40) and test_nums(-79, 1601, 80)
## observed that they're the same primes.
## figured the highest prime below 1000 in this chain was probably the value for b, and then just found the value for x to make the same parabola landingon all these primes

def is_prime(numbers):
  output = []
  for num in numbers:
    if num in primes:
      output.append(True)
    else:
      output.append(False)
  return output

print(is_prime(test_nums(-61, 971, 100)))
