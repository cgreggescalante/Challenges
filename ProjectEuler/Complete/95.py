# Amicable Chains
from tqdm import tqdm


def proper_divisor_sum(n):
    divisors = 1

    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divisors += i
            divisors += n // i

    return divisors


longest = 0
longest_element = 0
encountered = {}

for i in tqdm(range(1, 2000001)):
    try:
        a = encountered[i]
        continue
    except KeyError:
        encountered[i] = 0

    chain_length = 1
    smallest = i
    n = proper_divisor_sum(i)
    prev = {
        i: 0,
        n: 0
    }
    works = True

    while n != i and n != 1 and n <= 1000000:
        if n < smallest:
            smallest = n
        chain_length += 1
        n = proper_divisor_sum(n)
        try:
            a = prev[n]
            break
        except KeyError:
            prev[n] = 0

    if n <= 1000000 and n == i and chain_length > longest:
        longest = chain_length
        longest_element = smallest

print(longest_element)
