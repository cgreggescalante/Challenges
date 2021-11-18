# Find a k-Universal Circular String
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    k = int(file.readline())

out = ""
for i in range(2**k):
    b = bin(i)[2:]

    while len(b) < k:
        b = "0" + b

    if b not in out:
        works = False
        if works:
            continue
        overlap = 0
        for j in range(1, k):
            if out.endswith(b[:j]):
                overlap = j

        out += b[overlap:]

print(out)
