from useful import generate_number_of_primes as gp
from time import time
start = time()
primes = gp(32000)

def generate_pandigitals(digits):
    pandigitals = []
    digits = [str(x) for x in range(1, 10)]
    for i in digits:
        di = digits.remove(i)
        for j in di:
            dj = digits.remove(j)
            for k in dj:
                dk = digits.remove(k)
                for l in dk:
                    dl = digits.remove(l)
                    for m in dl:
                        dm = digits.remove(m)
                        for n in dm:
                            dn = digits.remove(n)
                            for o in dn:
                                do = digits.remove(o)
                                for p in do:
                                    dp = digits.remove(p)