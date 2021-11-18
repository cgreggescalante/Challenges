# Goldbach's Conjecture

primes = [True for _ in range(32001)]
p = 2

while p * p <= 32000:
    if primes[p]:
        for i in range(p * 2, 32001, p):
            primes[i] = False
    p += 1

primes[0] = False
primes[1] = False

primes = [i for i in range(len(primes)) if primes[i]]
n = int(input())

for _ in range(n):
    x = int(input())
    reps = []
    a = 0
    while a < len(primes) and primes[a] < x:
        b = 0
        while primes[a] + primes[b] < x and b < a:
            b += 1
        if primes[a] + primes[b] == x and b <= a:
            reps.append([primes[b], primes[a]])
        a += 1

    print(f"{x} has {len(reps)} representation(s)")
    for r in reps[::-1]:
        print(f"{r[0]}+{r[1]}")
    print()
