# Cold-puter Science

N = int(input())

t = map(int, input().split())

print(len([a for a in t if a < 0]))
