primes = []
composites = {}
current_number = 2
while len(primes) < 200000:
    if current_number not in composites:
        primes.append(current_number)
        composites[current_number ** 2] = [current_number]
    else:
        for factor in composites[current_number]:
            composites.setdefault(factor + current_number, []).append(factor)
        del composites[current_number]
    current_number += 1
counter = int(input())
nums = [int(x) for x in input().split()]
for num in nums:
    print(primes[num - 1], " ")
