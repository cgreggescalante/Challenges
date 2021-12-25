# Vanya and Lanterns

n, l = map(int, input().split())
lanterns = sorted(list(map(int, input().split())))

min_range = max(lanterns[0], l - lanterns[-1])
max_diff = 0
if n > 1:
    max_diff = max(lanterns[i + 1] - a for i, a in enumerate(lanterns[:-1]))

print(max(min_range, max_diff / 2))
