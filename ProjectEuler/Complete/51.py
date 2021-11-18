# Prime Digit Replacements
from Utilities.EratosthenesSieve import primes_in_range


def swap(n, key, target):
    s = str(n)
    result = 0
    for i in range(len(s)):
        result *= 10
        if key[i]:
            result += target
        else:
            result += int(s[i])

    return result


primes = primes_in_range(10**7)

for d in range(2, 7):
    options = []
    for i in range(1, 2**d - 1):
        option = []
        for s in bin(i)[2:]:
            option.append(int(s))
        while len(option) < d:
            option = [0] + option
        options.append(option)
    group = []
    check = {}
    for p in primes:
        if 10**(d - 1) < p < 10**d:
            check[p] = primes
            group.append(p)

    for p in group:
        for o in options:
            fam = []
            for i in range(10):
                x = swap(p, o, i)
                try:
                    a = check[x]
                    fam.append(x)
                except KeyError:
                    pass
            if len(fam) == 8:
                print(fam)
                quit(0)
