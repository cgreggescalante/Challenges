# Odd Gnome

n = int(input())

for _ in range(n):
    group = list(map(int, input().split()[1:]))
    for i, g in enumerate(group):
        if sorted(group[:i] + group[i + 1:]) == group[:i] + group[i + 1:]:
            print(i + 1)
            break
