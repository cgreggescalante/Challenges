# Pandigital Fibonacci Ends

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def pan(d):
    needed = nums[:]

    for n in d:
        try:
            needed.remove(n)
        except ValueError:
            return False

    return len(needed) == 0


n = 0
prev = 0
current = 1

while current < 10**10:
    temp = current
    current += prev
    prev = temp
    n += 1


while True:
    temp = current
    current += prev
    prev = temp
    n += 1
    if pan(str(current)[-9:]):
        print("   ", n + 1, current)
        if pan(str(current)[:9]):
            break
