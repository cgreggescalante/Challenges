# Prime Permutations
from Utilities.EratosthenesSieve import primes_in_range


def is_permutation(x, y):
    xs = [a for a in str(x)]
    ys = [a for a in str(y)]
    for i in xs:
        if i in ys:
            ys.remove(i)
    return len(ys) == 0


primes = [a for a in primes_in_range(9999) if a > 999]

combos = []

while len(primes) > 0:
    combo = [primes[0]]
    primes.pop(0)
    i = 0
    while i < len(primes):
        if is_permutation(primes[i], combo[0]):
            combo.append(primes[i])
            primes.pop(i)
        else:
            i += 1
    if len(combo) == 3:
        combos.append(combo)
    if len(combo) > 3:
        for start in range(len(combo) - 2):
            combos.append(combo[start:start+3])

filtered_combos = []
for i in combos:
    if i[2] - i[1] == i[1] - i[0]:
        filtered_combos.append(i)

for i in filtered_combos:
    print(i)