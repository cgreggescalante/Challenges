# Batter Up

n = int(input())

s = [a for a in map(int, input().split()) if a > -1]

print(sum(s) / len(s))
