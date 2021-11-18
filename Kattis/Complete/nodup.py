# No Duplicates

l = input().split()

d = set(l)

print("yes" if len(l) == len(d) else "no")
