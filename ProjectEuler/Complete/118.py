from Utilities.EratosthenesSieve import primes_in_range

primes = primes_in_range(10**8)


clean_primes = []

for a in primes:
    digits = [x for x in range(1, 10)]

    works = True

    for c in str(a):
        if int(c) in digits:
            digits.remove(int(c))
        else:
            works = False
            break

    if works:
        clean_primes.append(a)


def extend_group(group, previous, remaining_digits):
    count = 0

    for n in range(previous + 1, len(clean_primes)):
        if len(str(clean_primes[n])) > len(remaining_digits):
            break

        works = True

        for c in str(clean_primes[n]):
            if int(c) not in remaining_digits:
                works = False

        if works:
            next_digits = remaining_digits[:]
            for c in str(clean_primes[n]):
                next_digits.remove(int(c))

            if len(next_digits) == 0:
                count += 1
            else:
                count += extend_group(group + [clean_primes[n]], n, next_digits)

    return count


total = 0
print("Completed Pre-Processing")

for a in range(len(clean_primes)):
    print(clean_primes[a])
    prev = a
    group = [clean_primes[a]]
    digits = [x for x in range(1, 10)]

    for c in str(clean_primes[a]):
        digits.remove(int(c))

    total += extend_group(group, prev, digits)

print(total)