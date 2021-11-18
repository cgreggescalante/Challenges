# Digit Cancelling Fractions


def does_cancel(n, d):
    master = n / d

    n, d = str(n), str(d)

    matching = []
    new_fracs = []

    for i in range(len(n)):
        for j in range(len(d)):
            if n[i] == d[j]:
                a = 0 if i else 1
                b = 0 if j else 1
                matching.append([a, b])

    for pair in matching:
        new_n = n[pair[0]]
        new_d = d[pair[1]]
        if not new_d == '0':
            new_fracs.append(int(new_n) / int(new_d))

    for frac in new_fracs:
        if frac == master:
            return True
    return False


cancelers = []

for d in range(10, 100):
    for n in range(10, d):
        if not n % 10 == 0 and not d % 10 == 0:
            if does_cancel(n, d):
                cancelers.append([n, d])

top = 1
bottom = 1

for i in cancelers:
    top *= i[0]
    bottom *= i[1]

print(1 / (top / bottom))
