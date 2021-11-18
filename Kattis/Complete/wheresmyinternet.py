# Where's My Internet??

N, M = map(int, input().split())

connected = {1}

disconnected = {i for i in range(2, N+1)}
pairs = []

for _ in range(M):
    a, b = map(int, input().split())

    a_in = a in connected
    b_in = b in connected

    if a_in and not b_in:
        disconnected.remove(b)
        connected.add(b)
    if b_in and not a_in:
        disconnected.remove(a)
        connected.add(a)
    if not (a_in or b_in):
        pairs.append([a, b])

while True:
    d_len = len(disconnected)
    new_pairs = []
    while pairs:
        p = pairs.pop()
        a_in = p[0] in connected
        b_in = p[1] in connected

        if a_in and not b_in:
            disconnected.remove(p[1])
            connected.add(p[1])
        if b_in and not a_in:
            disconnected.remove(p[0])
            connected.add(p[0])
        if not (a_in or b_in):
            new_pairs.append(p)
    pairs = new_pairs
    if d_len == len(disconnected):
        break


if len(disconnected) == 0:
    print("Connected")

for i in sorted(disconnected):
    print(i)
