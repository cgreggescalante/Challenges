# Longest Increasing Subsequence
from math import ceil

with open("../Resources/rosalind_lgis.txt", "r") as file:
    file.readline()
    pi = list(map(int, file.readline().split()))


def increasing(arr):
    # P[k] stores predecessor of arr[k] in the longest increasing subsequence ending at arr[k]
    P = [0] * len(arr)
    # M[j] stores the index k of the smallest value arr[k] such that there is an increasing subsequence of length j
    # ending at arr[k] on the range k <= i
    M = [0] * (len(arr) + 1)

    # L is the length of the longest subsequence found so far
    L = 0
    for i in range(0, len(arr)):
        lo = 1
        hi = L
        while lo <= hi:
            mid = ceil((lo+hi)/2)
            if arr[M[mid]] < arr[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL-1]
        M[newL] = i

        if newL > L:
            L = newL

    S = [0] * L
    # arr[k] is the last value in the subsequence of length L
    k = M[L]
    for i in range(L-1, -1, -1):
        S[i] = arr[k]
        k = P[k]

    return S


def decreasing(arr):
    # P[k] stores predecessor of arr[k] in the longest increasing subsequence ending at arr[k]
    P = [0] * len(arr)
    # M[j] stores the index k of the smallest value arr[k] such that there is an increasing subsequence of length j
    # ending at arr[k] on the range k <= i
    M = [0] * (len(arr) + 1)

    # L is the length of the longest subsequence found so far
    L = 0
    for i in range(0, len(arr)):
        lo = 1
        hi = L
        while lo <= hi:
            mid = ceil((lo + hi) / 2)
            if arr[M[mid]] > arr[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        if newL > L:
            L = newL

    S = [0] * L
    # arr[k] is the last value in the subsequence of length L
    k = M[L]
    for i in range(L - 1, -1, -1):
        S[i] = arr[k]
        k = P[k]

    return S


print(' '.join(str(a) for a in increasing(pi)))
print(' '.join(str(a) for a in decreasing(pi)))
