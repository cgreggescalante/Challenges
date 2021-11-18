# I've Been Everywhere, Man

T = int(input())

for _ in range(T):
    s = set()
    n = int(input())
    for _ in range(n):
        s.add(input())
    print(len(s))
