# Boat Parts

P, N = map(int, input().split())

s = set()

i = 0
while i < N and len(s) < P:
    s.add(input())
    i += 1

if len(s) == P:
    print(i)
else:
    print("paradox avoided")
