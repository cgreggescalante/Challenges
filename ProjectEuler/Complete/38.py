# Pandigital Multiples


def is_permutation(a):
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in a:
        if x in b:
            b.remove(x)
        else:
            return False
    return len(b) == 0


def num_from_array(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i] * 10 ** (len(arr) - i - 1)
    return total


largest = 0

for n in range(1, 10000):
    required = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    nums = []
    i = 0
    while len(nums) < 9:
        i += 1
        nums.extend([int(i) for i in str(n * i)])

    if len(nums) == 9 and is_permutation(nums):
        x = num_from_array(nums)
        if x > largest:
            largest = x
            print(largest)

