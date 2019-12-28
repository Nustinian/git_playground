counter = int(input())
for i in range(counter):
    nums = [int(x) for x in input().split()]
    time = nums[0] / (nums[1] + nums[2])
    distance = time * nums[1]
    print(str(distance) + " ")