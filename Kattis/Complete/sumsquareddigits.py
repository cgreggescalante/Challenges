# Sum Squared Digits Function

P = int(input())


def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


for _ in range(P):
    K, b, n = map(int, input().split())

    print(K, sum([a * a for a in number_to_base(n, b)]))
