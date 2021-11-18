# CD

"""
    Current Implementations exceed the time limit of 2 seconds
"""

#
# M, N = map(int, input().split())
#
# while M + N > 0:
#     jack = {int(input()) for _ in range(M)}
#     jill = {int(input()) for _ in range(N)}
#     print(len(jack.intersection(jill)))
#     M, N = map(int, input().split())

M, N = map(int, input().split())

while M + N > 0:
    a = [input() for _ in range(M)]
    b = [input() for _ in range(N)]

    a_idx = 0
    b_idx = 0
    olap = 0

    while a_idx < M and b_idx < N:
        if a[a_idx] < b[b_idx]:
            a_idx += 1
        elif b[b_idx] < a[a_idx]:
            b_idx += 1
        else:
            olap += 1
            a_idx += 1
            b_idx += 1

    print(olap)
    M, N = map(int, input().split())
