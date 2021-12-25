# Line Them Up

names = [input() for _ in range(int(input()))]

s = sorted(names)
if names == s:
    print("INCREASING")
elif names == s[::-1]:
    print("DECREASING")
else:
    print("NEITHER")
