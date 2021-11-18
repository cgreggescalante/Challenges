# Generalised Hamming Numbers
import primesieve


def value(mask):
    p = 0
    for b, p in zip(primes, mask):
        p += b ** p
    return p


type = 100
target = 9
primes = primesieve.primes(type)[::-1]

maxes = []
prod = 1

for i in range(len(primes)):
    p = primes[i]
    j = 0
    while p ** j <= 10**target:
        j += 1
    maxes.append(j - 1)
    prod *= j - 1

poss = set()


def rec_e(digit=0, val=1, mask=None):
    if mask is None:
        mask = [0 for _ in range(len(primes))]
    if digit == len(primes):
        poss.add(val)
        return

    for d in range(maxes[digit], -1, -1):
        new_mask = mask[:]
        new_mask[digit] = d
        v = val * primes[digit] ** d
        if v <= 10 ** target:
            rec_e(digit + 1, v, new_mask)


rec_e()
print(len(poss))
