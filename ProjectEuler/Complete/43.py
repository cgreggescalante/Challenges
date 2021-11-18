digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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


def comb(digits, start):
    start -= 1
    return digits[start] * 100 + digits[start+1] * 10 + digits[start+2]


def test(digits):
    two = comb(digits, 2) % 2 == 0
    three = comb(digits, 3) % 3 == 0
    four = comb(digits, 4) % 5 == 0
    five = comb(digits, 5) % 7 == 0
    six = comb(digits, 6) % 11 == 0
    seven = comb(digits, 7) % 13 == 0
    eight = comb(digits, 8) % 17 == 0
    return two and three and four and five and six and seven and eight


def coagulate(digits):
    s = 0
    d = digits[::-1]
    for i in range(len(digits)):
        s += d[i] * 10 ** i
    return s


total = 0
counter = 0

while counter < 3628800:
    if test(digits):
        print(digits)
        total += coagulate(digits)

    digits = iterate(digits)

    if digits == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        break
    counter += 1

print(total)
