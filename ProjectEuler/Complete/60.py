# Prime Pair Sets
from Utilities.EratosthenesSieve import primes_in_range


def concat(a, b):
    sa = str(a)
    sb = str(b)

    return int(sa + sb)


primes = primes_in_range(10**8)
small_primes = [a for a in primes if a < 10**4]

check = {}

for p in primes:
    check[p] = 0

pairs = {}
sets = []

for i in range(len(small_primes)):
    matches = []
    for j in range(i+1, len(small_primes)):
        c = concat(small_primes[i], small_primes[j])
        c1 = concat(small_primes[j], small_primes[i])
        try:
            a = check[c]
            b = check[c1]
            matches.append(small_primes[j])
        except KeyError:
            continue
    if len(matches) >= 4:
        pairs[small_primes[i]] = matches
        for m in matches:
            sets.append([small_primes[i], m])

while len(sets[0]) < 5:
    new_sets = []

    for s in sets:
        overlap = pairs[s[0]]
        for o in overlap:
            works = True
            for x in s[1:]:
                if x in pairs:
                    if o not in pairs[x]:
                        works = False
                        break
                else:
                    works = False
            if works:
                new_sets.append(s + [o])

    sets = new_sets

for s in sets:
    print(s, sum(s))
