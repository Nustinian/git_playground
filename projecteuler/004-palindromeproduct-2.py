def is_palindrome(number):
  num = str(number)
  checks = len(num) // 2
  for i in range(checks):
    if num[i] == num[-1 - i]:
      continue
    else:
      return False
  return True

highest_palindrome = 0
a = 999
while a >= 100:
  if a % 11 == 0:
    b = 999
    increment = 1
  else:
    b = 990
    increment = 11
  while b >= a:
    if a * b <= highest_palindrome:
      break
    if is_palindrome(a * b):
      highest_palindrome = a * b
    b -= increment
  a -= 1

print(highest_palindrome)