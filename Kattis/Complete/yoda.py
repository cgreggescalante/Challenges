# Yoda

N = list(map(int, input()))
M = list(map(int, input()))

i = 1

while i <= len(N) and i <= len(M):
    if N[-i] > M[-i]:
        M[-i] = -1
    elif N[-i] < M[-i]:
        N[-i] = -1
    i += 1

N = [str(a) for a in N if a > -1]
M = [str(a) for a in M if a > -1]

if len(N) == 0:
    print("YODA")
else:
    print(int(''.join(N)))
if len(M) == 0:
    print("YODA")
else:
    print(int(''.join(M)))
