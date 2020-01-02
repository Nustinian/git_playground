import math
for i in range(int(input())):
    line = input().split()
    nums = [int(x) for x in line[1:]]
    average = sum(nums) / 14
    commission = average / 100
    deviation = 0
    for num in nums:
        deviation += (average - num) ** 2
    deviation /= 14
    deviation = math.sqrt(deviation)
    if deviation > 4 * commission:
        print(line[0], " ")