# Job Expenses

n = int(input())

print(-sum([i for i in list(map(int, input().split())) if i < 0]))
