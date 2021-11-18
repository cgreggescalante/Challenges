# Maximum Number of Divisors
from Utilities.Factoring import divisors


def S(u, k):
    div_count = []
    total = 0

    for n in range(u + 1):
        div_count.append(len(divisors(n, True)))

    max_val = div_count[0]
    pos = 0
    for j in range(1, k):
        if div_count[j] >= max_val:
            max_val = div_count[j]
            pos = j

    for i in range(u - k + 1):
        total += max_val

        if div_count[i + k - 1] > max_val:
            max_val = div_count[i + k - 1]
            pos = i + k
        elif pos == i:
            max_val = div_count[i + 1]
            pos = 0
            for j in range(1, k):
                if div_count[j + i] >= max_val:
                    max_val = div_count[j + i]
                    pos = j + i
    return total


print(S(1000, 10))
