# Primes with runs
from tqdm import tqdm

from Utilities.EratosthenesSieve import primes_in_range
from Utilities.PrimeTesting import is_prime


def count_repeats(n, d):
    s = str(n)
    count = 0
    for i in s:
        if int(i) == d:
            count += 1
    return count


def M(n):
    max_repeats = {}

    nums = {}
    for i in range(10):
        nums[i] = []
        max_repeats[i] = 0

    l = int((10**n - 10**(n-1)+1) / 20)
    t = tqdm(range(l))

    for p in primes:
        if p <
        for d in range(10):
            c = count_repeats(p, d)
            if c >= max_repeats[d]:
                if c == max_repeats[d]:
                    nums[d].append(p)
                if c > max_repeats[d]:
                    max_repeats[d] = c
                    nums[d] = [p]

    total = 0
    for i in range(10):
        total += sum(nums[i])
        print(i, sum(nums[i]), len(nums[i]), nums[i])
    return total


is_prime(1)
primes = primes_in_range(10**11)
print("Finished generating primes")
print(M(10))
