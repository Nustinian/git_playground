digit_fifths = [i ** 5 for i in range(10)]

def num_to_listnum(num):
  return [int(strnum) for strnum in str(num)]

def sum_digit_fifths(listnum):
  return sum([digit_fifths[num] for num in listnum])

def check_sums(num):
  if sum_digit_fifths(num_to_listnum(num)) == num:
    return True
  else:
    return False

answers = []
for i in range(300000):
  if check_sums(i):
    answers.append(i)
print(answers)
print(sum(answers))
