# Efficient exponentiation
from itertools import combinations_with_replacement


def branch(available):
    branches = set()
    available = set(available)
    to_remove = set()
    for a in available:
        if a > max(targets):
            to_remove.add(a)
    available.difference_update(to_remove)
    for comb in combinations_with_replacement(available, 2):
        s = sum(comb)
        if max(available) < s <= max(targets):
            na = available.copy()
            na.add(s)
            branches.add(frozenset(na))
    return branches


nodes = {frozenset([1])}
targets = {k for k in range(1, 201)}
total = 0

steps = 0
while True:
    for n in nodes:
        for t in range(1, 201):
            if t in targets and t in n:
                total += steps
                targets.remove(t)
        for t in range(1, 201):
            if t - 1 in targets and t - 1 in n:
                total += steps + 1
                targets.remove(t - 1)
    if len(targets) == 0:
        break
    else:
        print(len(targets), len(nodes), total, steps, sorted(targets))
    steps += 1
    new_nodes = set()
    for n in nodes:
        b = branch(n)
        new_nodes.update(b)
    nodes = new_nodes
    # print(len(nodes))

print(total)
