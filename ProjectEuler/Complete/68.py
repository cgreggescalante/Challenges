# Magic 5-gon Ring


def suffix(digits):

    i = len(digits) - 1
    while i > 0 and digits[i - 1] >= digits[i]:
        i -= 1

    return i


def iterate(digits):
    pivot = suffix(digits) - 1
    swap_index = -1
    for i in range(len(digits)-1, pivot, -1):
        if digits[i] > digits[pivot]:
            swap_index = i
            break

    digits[pivot], digits[swap_index] = digits[swap_index], digits[pivot]

    suff = digits[pivot + 1:]
    return digits[:pivot+1] + suff[::-1]


def check(digits):
    a = digits[0]
    if a > min([digits[3], digits[5], digits[7], digits[9]]):
        return False

    s = sum(digits[0:3])
    if s != digits[3] + digits[2] + digits[4]:
        return False
    if s != digits[5] + digits[4] + digits[6]:
        return False
    if s != digits[7] + digits[6] + digits[8]:
        return False
    if s != digits[9] + digits[8] + digits[1]:
        return False
    return True


def coagulate(d):
    n = [d[0], d[1], d[2], d[3], d[2], d[4], d[5], d[4], d[6], d[7], d[6], d[8], d[9], d[8], d[1]]
    n = [str(a) for a in n]

    return int(''.join(n))


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

solutions = []

biggest = 0

while True:
    if digits.index(10) not in [1, 2, 4, 6, 8]:
        if check(digits):
            v = coagulate(digits)
            if v > biggest:
                biggest = v
                print(biggest)
    digits = iterate(digits)

