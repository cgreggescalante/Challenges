# DRM Messages

l = input()

a = l[:len(l) // 2]
b = l[len(l) // 2:]

ac = sum(map(lambda x: ord(x) - 65, a))
bc = sum(map(lambda x: ord(x) - 65, b))

a = [(ord(i) - 65 + ac) % 26 for i in a]
b = [(ord(i) - 65 + bc) % 26 for i in b]

c = [(i + j) % 26 + 65 for i, j in zip(a, b)]

print(''.join(map(chr, c)))
