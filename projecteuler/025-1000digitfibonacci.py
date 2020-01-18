fibs = {}
def fib(number):
    if number in fibs:
        return fibs[number]
    elif number == 1:
        return 1
    elif number == 2:
        return 1
    else:
        fibs[number] = fib(number - 1) + fib(number - 2)
    return fibs[number]

i = 1
length = 1
while length < 1000:
    fib(i)
    i += 1  
    length = len(str(fib(i)))

print(i)