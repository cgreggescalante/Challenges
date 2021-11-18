# A Classy Problem

T = int(input())

d = {}

for _ in range(T):
    n = int(input())
    people = []
    for _ in range(n):
        spl = input().split()
        name = spl[0][:-1]
        cls = spl[1].split("-")
        people.append(cls[::-1] + [name])
    l = max(map(len, people))
    srted = []
    for p in people:
        while len(p) < l:
            p = p[:-1] + ["middle"] + [p[-1]]
        np = []
        for i in p[:-1]:
            if i == "upper":
                np.append("2")
            elif i == "middle":
                np.append("1")
            else:
                np.append("0")
        np = int(''.join(np))
        srted.append([np, p[-1]])
    srted.sort(key=lambda x: x[1], reverse=True)
    srted.sort(key=lambda x: x[0])
    for p in srted[::-1]:
        print(p[1])
    print("=" * 30)
