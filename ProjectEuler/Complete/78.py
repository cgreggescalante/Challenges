# Coin Partitions

"""
Cases :
n == k : 1
k == 1 : 1
k == 2 : n // 2
"""

known = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7}


def partition(n):
    if n in known:
        return known[n]

    add = True
    total = 0
    natural = 1
    odd = 1
    offset = 0

    while offset <= n:
        offset += odd
        odd += 2
        if offset > n:
            break
        p = partition(n - offset)
        total += p if add else -p

        offset += natural
        natural += 1
        if offset > n:
            break
        p = partition(n - offset)
        total += p if add else -p
        add = not add

    known[n] = total
    return total


i = 0
while True:
    p = partition(i)
    if p % 1000000 == 0:
        print(i, p)
        break
    i += 1
