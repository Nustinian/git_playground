def is_palindrome(number):
  num = str(number)
  checks = len(num) // 2
  for i in range(checks):
    if num[i] == num[-1 - i]:
      continue
    else:
      return False
  return True

highest = 0

for i in (100, 999):
  for j in (100, 999):
    if is_palindrome(i * j) and i * j > highest:
      highest = i * j

print(highest)
