efibs = [2, 8]
def next_even_fib():
  efibs.append(4 * efibs[-1] + efibs[-2])

while efibs[-1] <= 4000000:
  next_even_fib()

print(sum(efibs) - efibs[-1])
