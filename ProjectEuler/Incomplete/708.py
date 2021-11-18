# Twos Are All You Need
from tqdm import tqdm

from Utilities.Factoring import prime_factors

t = tqdm(range(10**9))
for i in range(1, 10**14):
    prime_factors(i, True)
    if i % 10**5 == 0:
        t.update()