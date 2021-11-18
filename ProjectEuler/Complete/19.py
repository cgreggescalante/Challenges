count = 0
sun = 0
for y in range(1901, 2001):

    leap = False
    if str(y).endswith('00') and y % 400 == 0:
        leap = True
    elif y % 4 == 0:
        leap = True

    for m in range(1, 13):

        current = 0

        if m in [1, 3, 5, 7, 8, 10, 12]:
            days = 31
        elif m in [4, 6, 9, 11]:
            days = 30
        elif m == 2 and leap:
            days = 29
        else:
            days = 28

        if count % 7 == 0:
            sun += 1

        count += days

print(sun)
