counter = int(input())
for i in range(counter):
    num = int(input())
    test_me = 2
    factors = ""
    while num != 1:
        if num % test_me == 0:
            num = num / test_me
            factors += str(test_me) + "*"
        else:
            test_me += 1
    print(factors[:-1] + " ")

