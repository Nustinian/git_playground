def factorial(number):
    if number > 1:
        return number * factorial(number - 1)
    if number == 1:
        return 1

counter = int(input())

for i in range(counter):
    info = [int(x) for x in input().split()]
    n, k = info[0], info[1]
    c = factorial(n) // (factorial(k) * factorial(n - k))
    print(str(c) + " ")