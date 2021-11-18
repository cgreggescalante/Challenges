# Electrical Outlets

N = int(input())

for _ in range(N):
    arr = list(map(int, input().split()))
    print(sum(arr[1:]) - arr[0] + 1)
