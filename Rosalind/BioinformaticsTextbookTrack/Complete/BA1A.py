# Compute the Number of Times a Pattern Appears in a Text
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    text = lines[0].strip()
    pattern = lines[1].strip()

t = 0
for i in range(len(text) - len(pattern) + 1):
    if text[i:].startswith(pattern):
        t += 1

print(t)
