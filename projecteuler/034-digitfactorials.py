factorials = {'0': 1}
for i in range(1, 10):
  factorials[str(i)] = factorials[str(i - 1)] * i

def sum_digits(number):
  return sum([factorials[x] for x in str(number)])

mysum = 0
for i in range(3,2550000):
  if sum_digits(i) == i:
    mysum += i

print(mysum)
