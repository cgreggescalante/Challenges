# Pandigital Fibonacci Ends

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def check(n):
    s = str(n)[:9]

    needed = nums[:]
    for c in s:
        if c in needed:
            needed.remove(c)
        else:
            return False

    if len(needed) != 0:
        return False

    s = str(n)[-9:]

    needed = nums[:]
    for c in s:
        if c in needed:
            needed.remove(c)
        else:
            return False

    return len(needed) == 0


n = 0
prev = 0
current = 1

while True:
    temp = current
    current += prev
    prev = temp
    n += 1
    if check(current):
        print(current)
        break
