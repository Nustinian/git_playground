primes = [2]
current_number = 3
while len(primes) < 200000:
    composite = False
    for prime in primes:
        if current_number % prime == 0:
            composite = True
            break
    if composite == False:
        primes.append(current_number)
    current_number += 1
print(primes[1000 - 1])