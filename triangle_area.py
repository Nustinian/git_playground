import math
counter = int(input())
for i in range(counter):
    nums = [int(x) for x in input().split()]
    area = abs((nums[0] * (nums[3] - nums[5]) + nums[2] * (nums[5] - nums[1]) + nums[4] * (nums[1] - nums[3])) / 2)
    print(str(area) + " ")