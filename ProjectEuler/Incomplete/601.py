# Divisibility Streaks


def streak(n):

    for k in range(32):
        if (n + k) % (k + 1) != 0:
            return k


def P(N):
    count = 2

    for i in range(5, 4**N, 2):
        val = streak(i)
        if i < 4**val:
            count += 1
            # print(i, count)

    return count


print(P(15))
