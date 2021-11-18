# Poker Hand
from collections import defaultdict

cards = input().split()

freq = defaultdict(int)

for c in cards:
    freq[c[0]] += 1

print(max(freq.values()))
