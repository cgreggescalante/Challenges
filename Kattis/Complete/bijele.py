# Bijele

full_set = [1, 1, 2, 2, 2, 8]

arr = list(map(int, input().split()))

print(' '.join([str(a - b) for a, b in zip(full_set, arr)]))
