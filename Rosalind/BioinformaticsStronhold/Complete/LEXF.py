# Enumerating k-mers Lexicographically


def base_convert(i, b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    return result


alpha = "A B C D".split()

n = 4

for i in range(n ** len(alpha)):
    key = base_convert(i, len(alpha))
    while len(key) < n:
        key = [0] + key

    print(''.join([alpha[a] for a in key]))