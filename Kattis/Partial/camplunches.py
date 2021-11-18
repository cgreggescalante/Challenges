# Camp Lunches

"""
n friend groups
k bins holding x lunches each
a children min
b children max

Combinations of n such that:
    sum(groups) % x == 0,
    sum(groups) < k * x,
    sum(groups) >= a,
    sum(groups) <= b
"""


def arr_sum(a, b):
    return sum([a[i] for i in range(len(a)) if b[i] == "1"])


n = int(input())
groups = sorted(list(map(int, input().split())))[::-1]
k, x, a, b = map(int, input().split())

top = 0

for comb in range(2**n):
    s = arr_sum(groups, format(comb, f"0{n}b"))
    if b >= s >= a and s > top and s % x == 0 and s <= k * x:
        top = s

print(top if top else "impossible")
