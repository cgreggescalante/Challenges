# Consecutive Prime Sum
from Utilities.EratosthenesSieve import primes_in_range

primes = primes_in_range(1000000)
prime_check = {}
for i in primes:
    prime_check[i] = 0

s = 0
i = 0
while s < 1000000:
    s += primes[i]
    i += 1
print(i, s)

best_l = 182
best_s = 0

for start in range(len(primes)):
    top = min(547, len(primes) - start + 1)
    for l in range(best_l, top):
        s = sum(primes[start:start+l])
        try:
            a = prime_check[s]
            if l > best_l:
                best_l = l
                best_s = s
                print(l, s)
        except KeyError:
            pass