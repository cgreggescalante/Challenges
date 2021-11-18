# Another Candies

T = int(input())

for _ in range(T):
    input()
    n = int(input())
    c = sum([int(input()) for _ in range(n)])
    print("NO" if c % n else "YES")
