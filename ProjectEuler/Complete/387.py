# Harshad Numbers
from Utilities.Misc import sum_digits
from Utilities.PrimeTesting import is_prime

limit = 10**14


strong = []


def evaluate(n):
    if n < limit / 10.0:
        f = (n + 0.0) / sum_digits(n)
        if int(f) == f:                 # Is Harshad
            if is_prime(f):             # Is strong Harshad
                strong.append(n)
            for i in range(10):
                evaluate(n * 10 + i)


for i in range(1, 10):
    evaluate(i)

result = 0

for i in strong:
    for j in range(10):
        if is_prime(i * 10 + j):
            result += i * 10 + j
            print(i * 10 + j)

print(result)