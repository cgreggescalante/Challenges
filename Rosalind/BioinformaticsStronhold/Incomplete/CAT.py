# Catalan Numbers and RNA Secondary Structures
import copy

pairs = {"A": "U", "U": "A", "C": "G", "G": "C"}

known_graphs = {
    0: [{}],
    2: [
        {0: 1}
    ],
}

graph_hashes = {
    0: [{}],
    2: [{1.5}]
}


def cantor(x, y):
    return ((x + y) * (x + y + 1) + y) / 2


def generate_pairs(n, f=0):
    if n in known_graphs:
        return [{k+f: v+f for k, v in g.items()} for g in known_graphs[n]]

    options = []
    h_options = []
    for x in range(1, n, 2):
        a = x - 1
        b = n - x - 1
        ap = generate_pairs(a, 1)
        bp = generate_pairs(b, x+1)
        for g1 in ap:
            for g2 in bp:
                d = {0: x} | g1 | g2
                options.append(d)
                h_options.append({cantor(x, y) for x, y in d.items()})
    known_graphs[n] = options
    graph_hashes[n] = h_options


def known_pairs_eval(s):
    if len(s) == 0:
        return 1
    if len(s) % 2 == 1:
        return 0
    else:
        graphs = known_graphs[len(s)]
        hashes = graph_hashes[len(s)]
        working_mask = [True for _ in range(len(graphs))]
        for i in range(len(graphs)):
            if not working_mask[i]:
                continue

            for a, b in graphs[i].items():
                if pairs[s[a]] != s[b]:
                    working_mask[i] = False
                    h = cantor(a, b)
                    for j in range(i + 1, len(graphs)):
                        if working_mask[j]:
                            if h in hashes[j]:
                                working_mask[j] = False

        return sum(working_mask)


def count_perfect_matchings(s):
    if len(s) < 33:
        return known_pairs_eval(s)

    c = 0
    for b in range(1, len(s), 2):
        if s[b] == pairs[s[0]]:
            inside = s[1:b]
            after = s[b+1:]
            if inside.count("G") == inside.count("C"):
                if len(s) > 40:
                    print(f"IN: {inside}, A: {after}")
                if len(inside) < len(after):
                    x = count_perfect_matchings(inside)
                    if x:
                        c += x * count_perfect_matchings(after)
                else:
                    x = count_perfect_matchings(after)
                    if x:
                        c += x * count_perfect_matchings(inside)
    return c


for n in range(4, 33, 2):
    generate_pairs(n)
    print(n)


with open("../Resources/rosalind_cat.txt", "r") as file:
    file.readline()
    s = ""
    line = file.readline().strip()
    while line:
        s += line
        line = file.readline().strip()

    print(count_perfect_matchings("UAGCGUGAUCAC"))
