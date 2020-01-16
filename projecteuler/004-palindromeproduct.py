def is_palindrome(number):
  num = str(number)
  checks = len(num) // 2
  for i in range(checks):
    if num[i] == num[-1 - i]:
      continue
    else:
      return False
  return True

print(is_palindrome(input("Enter number to check: ")))
