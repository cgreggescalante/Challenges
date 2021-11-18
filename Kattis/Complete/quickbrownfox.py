# Quick Brown Fox

alpha = "abcdefghijklmnopqrstuvwxyz"

n = int(input())

for _ in range(n):
    remain = alpha
    for i in input().lower():
        if i in remain:
            remain = remain.replace(i, "")
    if remain:
        print("missing", remain)
    else:
        print("pangram")
