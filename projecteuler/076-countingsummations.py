def with_up_to(x):
  target = 100
  numz = range(1, x + 1) 
  wayz = [1] + [0] * target
  for num in numz:
    for i in range(num, target + 1):
      wayz[i] += wayz[i - num]
  return wayz


target = 100
ways = [0] + [1] * (target)
nums = range(1, target) 
for num in nums:
  wayz = with_up_to(num)
  for i in range(num + 1, target + 1):
    ways[i] += wayz[i - num]

print(ways[-1])
