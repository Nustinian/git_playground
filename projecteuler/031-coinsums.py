def f2(x):
  return x // 2 + 1

f5_dict = {0: 0, 5: 4}
def f5(x):
  if x in f5_dict:
    return f5_dict[x]
  else:
    f5_dict[x] = f5(x - 5) + f2(x)
  return f5_dict[x]

f10_dict = {0: 0}
def f10(x):
  if x in f10_dict:
    return f10_dict[x]
  else:
    repeats = x // 10
    answer = f5(x)
    for i in range(1, repeats):
      answer += f5(x - 10 * i)
    if x % 10 == 0:
      answer += 1
    f10_dict[x] = answer
  return f10_dict[x]

f20_dict = {0: 0}
def f20(x):
  if x in f20_dict:
    return f20_dict[x]
  else:
    repeats = x // 20
    answer = f10(x)
    for i in range(1, repeats + 1):
      answer += f10(x - 20 * i) 
    if x % 20 == 0:
      answer += 1
    f20_dict[x] = answer
  return f20_dict[x]

f50_dict = {0: 0}
def f50(x):
  if x in f50_dict:
    return f50_dict[x]
  else:
    repeats = x // 50
    answer = f20(x)
    for i in range(1, repeats):
      answer += f20(x - 50 * i)
    if x % 50 == 0:
      answer += 1
    f50_dict[x] = answer
  return f50_dict[x]

f100_dict = {0: 0}
def f100(x):
  if x in f100_dict:
    return f100_dict[x]
  else:
    repeats = x // 100
    answer = f50(x)
    for i in range(1, repeats):
      answer += f50(x - 100 * i)
    if x % 100 == 0:
      answer += 1
    f100_dict[x] = answer
  return f100_dict[x]

f100(200)
print(f100_dict[200] + 1)
