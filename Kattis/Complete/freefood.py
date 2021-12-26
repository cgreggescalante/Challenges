# Free Food

n = int(input())
days = set()

for _ in range(n):
    s, e = map(int, input().split())
    days.update(list(range(s, e + 1)))

print(len(days))
