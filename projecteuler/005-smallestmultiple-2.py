from math import sqrt, log
def generate_primes(upper_limit):
    primes = []
    composites = {}
    current_number = 2
    while current_number < upper_limit:
        if current_number not in composites:
            primes.append(current_number)
            composites[current_number ** 2] = [current_number]
        else:
            for factor in composites[current_number]:
                composites.setdefault(factor + current_number, []).append(factor)
            del composites[current_number]
        current_number += 1
    return primes

def smallest_multiple(upper_limit):
    primes = generate_primes(upper_limit)
    multiple = 1
    for prime in primes:
        times = int(log(upper_limit, prime))
        for i in range(times):
            multiple *= prime
    return multiple


print(smallest_multiple(300))