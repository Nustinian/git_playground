collatz_dict = {}

def collatz(number):
    if number not in collatz_dict:
        if number == 1:
            collatz_dict[number] = 1
        elif number % 2 == 0:
            collatz_dict[number] = collatz(number // 2) + 1
        else:
            collatz_dict[number] = collatz(3 * number + 1) + 1
    return collatz_dict[number]

longest = [0, 0]

for i in range(500000, 1000001):
    cake = collatz(i)
    if cake > longest[0]:
        longest = [cake, i]
print(longest)