primes = []
composites = {}
current_number = 2
while current_number < 3000001:
    if current_number not in composites:
        primes.append(current_number)
        composites[current_number ** 2] = [current_number]
    else:
        for factor in composites[current_number]:
            composites.setdefault(factor + current_number, []).append(factor)
        del composites[current_number]
    current_number += 1

for i in range(int(input())):
    nums = [int(x) for x in input().split()]
    print((primes.index(nums[1]) - primes.index(nums[0]) + 1), " ")
