# Hanging Out on the Terrace

l, x = map(int, input().split())
current = 0
fails = 0

for _ in range(x):
    event, n = input().split()
    n = int(n)
    if event == "enter":
        if n + current > l:
            fails += 1
            continue
        current += n
    else:
        current -= n

print(fails)
