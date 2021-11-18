# Circular Logic

count = 0


def evaluate(a, b, c, d, e, f):
    left = [a, b, c, d, e, f]
    right = [b, c, d, e, f]
    if a + (b and c) == 1:
        right.append(1)
    else:
        right.append(0)

    for i in range(len(right)):
        if right[i] + left[i] == 2:
            return False

    return True


for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        count += evaluate(a, b, c, d, e, f)

print(count)