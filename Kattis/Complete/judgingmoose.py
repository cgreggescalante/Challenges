# Judging Moose

l, r = map(int, input().split())

if l + r:
    print("Odd" if l - r else "Even", end=" ")

    print(max([l, r]) * 2)
else:
    print("Not a moose")
