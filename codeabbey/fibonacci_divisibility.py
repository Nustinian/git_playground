fibonacci_numbers = [1, 2]
while len(fibonacci_numbers) < 10000:
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

counter = int(input())
nums = [int(x) for x in input().split()]
for num in nums:
    for index, fib in enumerate(fibonacci_numbers):
        if fib % num == 0:
            print(str(index + 2) + " ")
            break
