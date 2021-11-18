# Convergents of 3


def add(n, frac):
    frac[0] += frac[1] * n
    return frac


def flip(frac):
    return [frac[1], frac[0]]


def sum_digits(x):
    s = str(x)[::-1]
    total = 0
    for i in s:
        total += int(i)
    return total

vals = []

k = 1

while len(vals) < 101:
    vals.append(1)
    vals.append(2 * k)
    vals.append(1)
    k += 1

vals = vals[:99][::-1]

print(vals)

fraction = [0, 1]

for i in range(len(vals)):
    fraction = add(vals[i], fraction)
    fraction = flip(fraction)

fraction = add(2, fraction)

print(str(fraction[0]))
print(sum_digits(fraction[0]))