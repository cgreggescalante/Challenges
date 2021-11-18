# Forced Choice

N, P, S = map(int, input().split())

cards = {i for i in range(1, N+1)}

for _ in range(S):
    sel = set([i for i in map(int, input().split()[1:])])
    if P in sel:
        print("KEEP")
        cards = sel
    else:
        print("REMOVE")
        cards -= sel
