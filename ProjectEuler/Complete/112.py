def is_increasing(num):
    num = str(num)
    for i in range(1, len(num)):
        if num[i] < num[i-1]:
            return False
    return True


def is_decreasing(num):
    num = str(num)
    for i in range(1, len(num)):
        if num[i] > num[i - 1]:
            return False
    return True

n = 1
b = 0

while not b / n == .99:
    n += 1
    if not is_decreasing(n) and not is_increasing(n):
        b += 1
        print(n)