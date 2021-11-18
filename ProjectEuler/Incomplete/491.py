# Double Pandigital Number divisible by 11
from Utilities.LexicographicPermutations import iterate_digit_array

num = [1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]

final = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0]


def as_int(arr):
    t = 0
    for i in arr:
        t *= 10
        t += i
    return t


count = 0
while num is not final:
    i = as_int(num)
    if i % 11 == 0:
        count += 1
        if count % 20000 == 0:
            print(count, i)
    num = iterate_digit_array(num)
    while num[0] == 0:
        num = iterate_digit_array(num)

print(count)
