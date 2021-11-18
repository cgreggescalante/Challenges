# Stand on Zanzibar

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()[:-1]))
    s = 0
    for i in range(len(arr) - 1):
        if arr[i] * 2 < arr[i + 1]:
            s += arr[i + 1] - (arr[i] * 2)

    print(s)
