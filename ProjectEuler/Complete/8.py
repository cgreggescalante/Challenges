# Largest Product in a Series

num = ""

with open("../Resources/number8", "r") as file:
    file = file.readlines()

    for a in file:
        num += a.strip()

num = [int(a) for a in num]


def prod(arr):
    a = 1
    for i in arr:
        a *= i
    return a


m = 0

for i in range(len(num) - 13):
    p = prod(num[i:i+13])
    if p > m:
        m = p

print(m)
