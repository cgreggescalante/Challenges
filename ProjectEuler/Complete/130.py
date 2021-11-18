# Composites with Prime Repunit Property
from Utilities.EratosthenesSieve import primes_in_range


def R(k):
    s = '1' * k
    return int(s)


def A(n):
    k = 1

    while True:
        if R(k) % n == 0:
            return k
        k += 1


primes = primes_in_range(10**6)[1:]
total = 0
count = 0
i = 3

while count < 25:
    if i == primes[0]:
        primes = primes[1:]
    elif i % 10 != 5:
        a = A(i)
        if (i - 1) % a == 0:
            count += 1
            total += i
            print(count, i)
    i += 2

print(total)