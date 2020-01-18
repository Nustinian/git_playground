from useful import get_all_factors as gf

checked = []
def d(n):
    if n == 0:
        return 0
    factors = gf(n)
    factors.remove(n)
    return sum(factors)

def amicable_check(n):
    global thesum
    first = d(n)
    second = d(first)
    if second == n and n not in checked and n != first:
        amicables.append(n)
        amicables.append(first)
    checked.append(n)
amicables = []

for i in range(1, 10000):
    if i not in checked:
        amicable_check(i)
final = set(amicables)
print(final)
print(sum(final))