# Paper sheets of standard sizes: an expected-value problem
from itertools import permutations

print(len(list(permutations([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4], 15))))
envelope = [1, 1, 1, 1]


def evaluate(envelope, remain):
    count = 0
    options = 0

    if sum(envelope) == 1:
        count += 1

    if remain > 0:
        for i in range(4):
            if envelope[i]:
                options += 1
                new_envelope = envelope[:]
                new_envelope[i] -= 1
                for j in range(i+1, 4):
                    new_envelope[j] += 1
                # print(remain, envelope, new_envelope)
                nc, no = evaluate(new_envelope, remain - 1)
                count += nc
                options += no

    return count, options


c, o = evaluate(envelope, [1, 2, 4, 8])

print(f"{c} / {o} = {round(c / o, 6)}")
