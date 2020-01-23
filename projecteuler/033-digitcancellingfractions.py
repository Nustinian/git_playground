def digit_cancel(numerator, denominator, char):
  if denominator % 10 == 0:
    return 0
  num = [x for x in str(numerator)]
  num.remove(char)
  num = int(num[0])
  denom = [x for x in str(denominator)]
  denom.remove(char)
  denom = int(denom[0])
  return num / denom

for i in range(10, 100):
  for j in range(i + 1, 100):
    for char in str(i):
      if char in str(j):
        if digit_cancel(i, j, char) == i / j:
          print(i, j)

