# Prime Power Triples

from Utilities.EratosthenesSieve import primes_in_range

primes = primes_in_range(10000)

nums = {}
squares = [a**2 for a in primes]
cubes = [a**3 for a in primes]
fourths = [a**4 for a in primes]

for a in squares:
    for b in cubes:
        if a + b > 50000000:
            break
        for c in fourths:
            val = a + b + c
            if val > 50000000:
                break
            nums[val] = 0

print(len(nums))
