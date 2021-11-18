# ICPC Awards

N = int(input())

unis = []
awards = []

for _ in range(N):
    if len(unis) == 12:
        break
    l = input().split()
    if l[0] in unis:
        continue
    unis.append(l[0])
    awards.append(' '.join(l))

print("\n".join(awards))
