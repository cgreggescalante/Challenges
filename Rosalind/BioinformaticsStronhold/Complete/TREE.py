# Completing a Tree

adjacency = []

with open("../Resources/rosalind_tree.txt", 'r') as file:
    lines = file.readlines()
    n = int(lines[0])

    for line in lines[1:]:
        adjacency.append([int(a) for a in line.split()])


adjacency += [[a] for a in range(1, n+1)]

i = 0
while i < len(adjacency):
    for a in adjacency[i]:
        j = i + 1
        while j < len(adjacency):
            if a in adjacency[j]:
                adjacency[i] += [c for c in adjacency[j] if c not in adjacency[i]]
                adjacency = adjacency[:j] + adjacency[j+1:]
            else:
                j += 1
    i += 1

print(len(adjacency) - 1)
