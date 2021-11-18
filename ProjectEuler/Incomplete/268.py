# Counting Numbers With At Least Four Distinct Prime Factors Less Than 100
import primesieve

low_primes = primesieve.primes(100)

counter = [0 for _ in range(len(low_primes))]


def valid():
    return len([a for a in counter if a > 0]) >= 4


i = 0

