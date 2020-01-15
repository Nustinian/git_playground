sum = 2
num1 = 1
num2 = 2
current = 0
while current <= 4000000:
  current = num1 + num2
  if current % 2 == 0:
    sum += current
  num1 = num2
  num2 = current
print(current)
print(sum)