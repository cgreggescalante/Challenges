# Above Average

C = int(input())

for _ in range(C):
    line = list(map(int, input().split()))
    n = line[0]
    line = line[1:]
    avg = sum(line) / n
    print(f"{len([a for a in line if a > avg]) / n * 100:2.3f}%")
