# Square Root Smooth Numbers
import primesieve

primes = primesieve.primes(10**7)

coefficients = [0] * len(primes)

for i in range(len(coefficients)):
    c = 1
    while c * primes[i] < 10000000000:
