from useful import get_all_factors as gf
from functools import reduce

def is_abundant(x):
    if sum(gf(x)) - x > x:
        return True

abundants = []
for i in range(12, 28120):
    if is_abundant(i):
        abundants.append(i)

summable = [False for x in range(28123)]
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] < 28123:
            if summable[abundants[i] + abundants[j]] == False:
                summable[abundants[i] + abundants[j]] = True

answer = 0
for i in range(len(summable)):
    if summable[i] == False:
        answer += i

print(answer)