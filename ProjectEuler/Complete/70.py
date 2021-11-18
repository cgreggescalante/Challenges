# Totient Permutation

def totient(n):
    phi = [i for i in range(n+1)]

    for i in range(2, n+1):
        if phi[i] == i:
            for j in range(i, n+1, i):
                phi[j] -= phi[j] / i

    return [int(i) for i in phi]


def is_perm(a, b):
    if len(str(a)) == len(str(b)):
        al = sorted([int(x) for x in str(a)])
        bl = sorted([int(x) for x in str(b)])

        return al == bl
    return False


low = 10**10
ts = totient(10**7)

for i in range(2, len(ts)):
    if i / ts[i] < low:
        if is_perm(i, ts[i]):
            low = i / ts[i]
            print(i, ts[i])
