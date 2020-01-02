counter = int(input())
for i in range(counter):
    nums = [int(x) for x in input().split()]
    a = nums[0] % 6 + 1
    b = nums[1] % 6 + 1
    c = a + b
    print(str(c) + " ")