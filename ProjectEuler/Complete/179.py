# Consecutive Positive Divisors
from tqdm import tqdm

arr = [2 for i in range(10**7)]
print("Initialized")

for i in tqdm(range(2, 10**7)):
    for j in range(i*2, 10**7, i):
        arr[j] += 1

print("Completed Factoring")
print("Counting Factors")

c = 0
for i in tqdm(range(2, 10**7-1)):
    if arr[i] == arr[i+1]:
        c += 1

print(c)
