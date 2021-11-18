# Reconstruct a String from its Paired Composition
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    j, d = map(int, file.readline().split())
    pairs = [f"{'-' * d}".join(line.strip().split("|")) for line in file.readlines()]


def valid(a, b):



def combine(a, b, i):
    out = ""
    j = 0
    while j < len(b) and j < len(a) - i:
        if a[j + i] == "-" and b[j] == "-":
            out += "-"
        elif a[j + i] == "-":
            out += b[j]
        else:
            out += a[j + i]
        j += 1
    while j < len(b):
        out += b[j]
        j += 1
    while j < len(a) - i:
        out += a[j + i]
    return a[:i] + out


for a in range(len(pairs)):
    for b in range(len(pairs)):
        if a == b:
            continue
        if valid(pairs[a], pairs[b]):
            print(pairs[a], pairs[b])
