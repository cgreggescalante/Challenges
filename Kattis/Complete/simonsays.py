# Simon Says

N = int(input())

for _ in range(N):
    s = input()
    if s.startswith("Simon says"):
        print(s[11:])
