def suffix(digits):
    i = len(digits) - 1
    while i > 0 and digits[i - 1] >= digits[i]:
        i -= 1

    return i


def iterate_digit_array(digits):
    pivot = suffix(digits) - 1
    swap_index = -1
    for i in range(len(digits)-1, pivot, -1):
        if digits[i] > digits[pivot]:
            swap_index = i
            break

    digits[pivot], digits[swap_index] = digits[swap_index], digits[pivot]

    suff = digits[pivot + 1:]
    return digits[:pivot+1] + suff[::-1]
