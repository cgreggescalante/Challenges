import primesieve

primes = primesieve.primes(1000000)
prime_check = {}
for p in primes:
    prime_check[p] = 0

count = 0


def rotate(n):
    a = str(n)
    return int(a[1:] + a[0])


def circular(p):
    a = str(p)
    for s in a:
        if s in "024568":
            return False
    n = rotate(p)
    while n != p:
        try:
            a = prime_check[n]
        except KeyError:
            return False
        n = rotate(n)
    return True


for p in primes:
    if p < 10:
        count += 1
    elif circular(p):
        count += 1

print(count)
