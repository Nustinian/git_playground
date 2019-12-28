def collatz_step(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return (3 * number) + 1

def collatz_counter(number):
    counter = 0
    while number != 1:
        number = collatz_step(number)
        counter += 1
    return counter

trash = int(input())
nums = [int(x) for x in input().split()]
for num in nums:
	steps = collatz_counter(num)
	print(str(steps) + " ")