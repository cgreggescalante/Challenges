# Vauvau

A, B, C, D = map(int, input().split())

P, M, G = map(int, input().split())

m = ["both", "one", "none"]

PA = P % (A + B)
PB = P % (C + D)
PA = PA if PA > 0 else A + 1
PB = PB if PB > 0 else C + 1
P = (PA > A) + (PB > C)

MA = M % (A + B)
MB = M % (C + D)
MA = MA if MA > 0 else A + 1
MB = MB if MB > 0 else C + 1
M = (MA > A) + (MB > C)

GA = G % (A + B)
GB = G % (C + D)
GA = GA if GA > 0 else A + 1
GB = GB if GB > 0 else C + 1
G = (GA > A) + (GB > C)

print(m[P])
print(m[M])
print(m[G])
