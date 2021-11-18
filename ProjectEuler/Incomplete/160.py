# Factorial trailing digits
from tqdm import tqdm

N = 1000000000000
p = 1
for t in tqdm(range(2, N+1)):
    p *= t
    while p % 10 == 0:
        p //= 10
    p %= 10**5

print(p)
