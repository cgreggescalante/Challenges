# Pet

top = 0
top_i = 0

for i in range(5):
    s = sum(map(int, input().split()))
    if s > top:
        top = s
        top_i = i + 1

print(top_i, top)
