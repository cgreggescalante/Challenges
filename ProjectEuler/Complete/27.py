# Quadratic Primes
from Utilities.PrimeTesting import is_prime

longest = 0
best_prod = 0

for a in range(-999, 1000):
    print(a)
    for b in range(-1000, 1001):
        n = 0

        while True:
            val = n**2 + (a * n) + b
            if not is_prime(val):
                n -= 1
                break
            n += 1

        if n > longest:
            best_prod = a * b
            longest = n
            print("     ", longest)

print(longest, best_prod)
