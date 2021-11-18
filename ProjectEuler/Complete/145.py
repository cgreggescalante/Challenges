def reverse(x):
    return int(str(x)[::-1])


def odd(x):
    for d in str(x):
        if int(d) % 2 == 0:
            return False
    return True


def viable(x):
    if x % 10 == 0:
        return False
    if 90000000 <= x <= 100000000:
        return False
    if 900000 <= x <= 2000000:
        return False
    if 10000 <= x <= 100000:
        return False
    s = str(x)
    if (int(s[0]) + int(s[-1])) % 2 == 0:
        return False
    return True


def check(x):
    if odd(reverse(x) + x):
        return 1
    return 0


count = 0
checked = 0
x = 1
cap = 10**9
while x < cap:
    start = 0

    leading = int(str(x)[0])
    step = x // leading

    if leading % 2 == 0:
        start = 1

    for i in range(x + start, x + step, 2):
        if viable(i):
            checked += 1
            count += check(i)

    x += step
    print((x * 100.0) / cap)

print(checked)
print(count)
print("")

#
# count = 0
# checked = 0
# step = 1000
# for i in range(0, 1000):
#     checked += 1
#     if viable(i):
#         count += check(i)
#     if i % 100 == 0:
#         print(i, count)
#
# print(checked)
# print(count)
