# Magic Trick

s = input()

if len({a for a in s}) == len(s):
    print(1)
else:
    print(0)
