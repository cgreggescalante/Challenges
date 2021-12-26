# Dice Game

g = sum(map(int, input().split()))
e = sum(map(int, input().split()))

if g == e:
    print("Tie")
else:
    print("Emma" if e > g else "Gunnar")
