def search_for_spot(T, nums):
    for i in range(len(nums)):
        if nums[i] > T:
            return i

def insert_num(current, T, nums, spot):
    for i in range(current, spot, -1):
        nums[i] = nums[i - 1]
    nums[spot] = T
    return current - spot

counter = int(input())
nums = [int(x) for x in input().split()]
current_max = 0
for i in range(1, counter):
    if nums[i] > current_max:
        current_max = nums[i]
        print("0 ")
        continue
    else:
        T = nums[i]
        spot = search_for_spot(T, nums)
        swaps = insert_num(i, T, nums, spot)
        print(swaps, " ")
