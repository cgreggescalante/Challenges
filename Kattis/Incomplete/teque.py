# Teque

N = int(input())

teque = []

for _ in range(N):
    s, x = input().split()
    x = int(x)

    if s == "get":
        print(teque[x])
    if s == "push_front":
        teque.insert(0, x)
    if s == "push_middle":
        teque.insert((len(teque) + 1) // 2, x)
    if s == "push_back":
        teque.append(x)
