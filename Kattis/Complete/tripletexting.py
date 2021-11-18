# Triple Texting

s = input()

l = len(s) // 3

a, b, c = s[:l], s[l:2*l], s[2*l:]


def check(a, b, c):
    if a == b or a == c:
        return a
    else:
        return c


for i in range(l):
    print(check(a[i], b[i], c[i]), end="")
