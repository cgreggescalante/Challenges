# Flexible Spaces

w, p = map(int, input().split())

partitions = [0] + list(map(int, input().split())) + [w]

sizes = set()

for i in range(p + 2):
    for j in range(i + 1, p + 2):
        sizes.add(partitions[j] - partitions[i])

print(' '.join(map(str, sorted(sizes))))
