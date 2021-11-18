# Digit Factorial Chains


def factorial(n):
    if n < 2:
        return 1
    return factorial(n-1) * n


def sum_digits(n):
    s = str(n)
    total = 0
    for i in s:
        total += mapped[i]
    return total

mapped = {
    "0": 1,
    "1": 1,
    "2": 2,
    "3": 6,
    "4": 24,
    "5": 120,
    "6": 720,
    "7": 5040,
    "8": 40320,
    "9": 362880,
}


def chain_length(n):
    a = sum_digits(n)
    length = 1
    chain = [n]
    while a not in chain:
        chain.append(a)
        a = sum_digits(a)
        length += 1
    if length == 60:
        return 1
    return 0


t = 0
for i in range(1000000):
    print(i)
    t += chain_length(i)

print(t)
