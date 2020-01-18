from math import sqrt
from useful import prime_factorize as pf
from time import time

start = time()

def get_divisors(number):
    factors = pf(number)
    uniques = set(factors)
    divisors = 1
    for unique in uniques:
        divisors *= factors.count(unique) + 1
    return divisors

number = 1
divisors = get_divisors(number)
i = 2
while divisors < 500:
    number += i
    divisors = get_divisors(number)
    if divisors > 500:
        print(number)
        print(divisors)
    i += 1


finish = time()
print(finish - start)