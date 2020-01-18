from math import sqrt
from useful import generate_number_of_primes as gp
from time import time

start = time()
primes = gp(1476)

def get_divisors(number):
    prime_factors = []
    i = 0
    limit = int(sqrt(number))
    if primes[i] > limit:
        prime_factors.append(primes[i])
    while number > 1 and primes[i] <= limit:
        if number % primes[i] == 0:
            prime_factors.append(primes[i])
            number /= primes[i]
            limit = int(sqrt(number))
            if primes[i] > limit:
                prime_factors.append(number)
        else:
            i += 1
            if primes[i] > limit:
                prime_factors.append(number)
    uniques = set(prime_factors)
    divisors = 1
    for unique in uniques:
        divisors *= prime_factors.count(unique) + 1
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