# Totient Maximum


def totient(n):
    result = n

    p = 2
    while p*p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result *= 1.0 - (1.0 / p)
        p = p + 1

    if n > 1:
        result *= 1.0 - (1.0 / n)

    return int(result)


max_val = 0
max_n = 0
n = 2

for n in range(2, 1000000, 2):
    p = totient(n)
    if n / p > max_val:
        max_val = n / p
        max_n = n
        print(max_val)

print(max_val, max_n)
