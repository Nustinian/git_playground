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
for i in range(101, 1000):
    for j in range(101, 1000):
        if is_palindrome(i * j) and (i * j) > highest_palindrome:
            highest_palindrome = i * j

print(highest_palindrome)