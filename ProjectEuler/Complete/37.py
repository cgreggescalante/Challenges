# Truncatable Primes
from Utilities.PrimeTesting import is_prime


def truncate_right(x):
    if x < 10:
        return 0
    s = str(x)
    return int(s[:-1])


def truncate_left(x):
    if x < 10:
        return 0
    s = str(x)
    return int(s[1:])


def test_right(x):
    test = truncate_right(x)
    while is_prime(test):
        test = truncate_right(test)
        if test == 0:
            return True
    return False


def test_left(x):
    test = truncate_left(x)
    while is_prime(test):
        test = truncate_left(test)
        if test == 0:
            return True
    return False


primes = [23]

n = 11

while len(primes) < 11:
    p = 1

    e = n % 10

    if e in [1, 5]:
        n += 2

    while True:
        test = (n - n % 10**p) // 10**p

        if test == 0:
            break

        if test % 2 == 0 and test != 2:
            n += 10**p

        if test == 1:
            n -= n % 10**p
            n += 2 * 10**p + 1
            p = 1

        p += 1

    if is_prime(n):
        if test_right(n):
            if test_left(n):
                primes.append(n)

    n += 2

print(primes)
print(sum(primes))
