from decimal import *

getcontext().prec = 5000

def find_pattern(strnum):
  first_three = strnum[:3]
  for i in range(len(strnum)):
    if i > 4:
      last_three = strnum[i - 2:i + 1]
      if last_three == first_three:
        until_now = strnum[:i - 2]
        same_length = strnum[i - 2:i + len(until_now) - 2]
        if same_length == until_now:
          return len(same_length) 
        else:
          return 0
  return 0

longest = 0
answer = 0
for i in range(1, 1000):
  d = str(1 / Decimal(i))[2:]
  cake = find_pattern(d)
  if cake > longest:
    longest = cake
    answer = i
print(answer, longest)
