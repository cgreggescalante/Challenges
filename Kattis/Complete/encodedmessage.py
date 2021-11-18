# Encoded Message

n = int(input())

for _ in range(n):
    l = input()
    s = int(len(l)**.5)

    print(''.join([l[i+s*j] for i in range(s-1, -1, -1) for j in range(s)]))
