# Exploring string for which only one character comes lexicographically after its neighbor to the left

def rec_e(chars, prev=None):
    options = []
    if prev is None:
        prev = 25
    if chars == 1:
        return [[a] for a in range(prev + 1)]
    for c in range(prev + 1):
        for a in rec_e(chars - 1, c):
            options.append([c] + a)
    return options


n = 3
total = 0
valid = set()
for a in rec_e(n):
    for i in range(1, n):
        for j in range(a[i - 1] + 1, 26):
            v = ''.join(map(lambda x: chr(x + 65), a[:i] + [j] + a[i + 1:]))
            print(v)
            valid.add(v)

print(len(valid))
