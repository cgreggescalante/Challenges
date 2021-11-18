# Pseudo-Fortunate Numbers
import primesieve

primes =    [2,  3,  5,  7, 11, 13, 17, 19, 23]
powers =    [1,  0,  0,  0, 0,  0,  0,  0,  0]
power_max = [29, 18, 11, 8, 6,  5,  3,  3,  1]
nums = []

for a in range(1, 30):
    a2 = 2**a
    nums.append(a2)
    for b in range(1, 19):
        b2 = a2 * 3**b
        if b2 > 10**9:
            break
        nums.append(b2)
        for c in range(1, 12):
            c2 = b2 * 5**c
            if c2 > 10 ** 9:
                break
            nums.append(c2)
            for d in range(1, 9):
                d2 = c2 * 7**d
                if d2 > 10 ** 9:
                    break
                nums.append(d2)
                for e in range(1, 7):
                    e2 = d2 * 11 ** e
                    if e2 > 10 ** 9:
                        break
                    nums.append(e2)
                    for f in range(1, 6):
                        f2 = e2 * 13 ** f
                        if f2 > 10 ** 9:
                            break
                        nums.append(f2)
                        for g in range(1, 4):
                            g2 = f2 * 17 ** g
                            if g2 > 10 ** 9:
                                break
                            nums.append(g2)
                            for h in range(1, 4):
                                h2 = g2 * 19 ** h
                                if h2 > 10 ** 9:
                                    break
                                nums.append(h2)
                                for i in range(1, 2):
                                    i2 = h2 * 23 ** i
                                    if i2 > 10 ** 9:
                                        break
                                    nums.append(i2)

primes = primesieve.primes(10**9)
p_index = 0
total = 0
pseudos = {}

for n in sorted(nums):
    while primes[p_index] <= n + 1:
        p_index += 1

    pseudos[primes[p_index] - n] = 0

print(sum(pseudos.keys()))