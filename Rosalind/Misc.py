import random
from itertools import combinations, combinations_with_replacement


def hamming_distance(a, b):
    return sum((1 for i in range(len(a)) if a[i] != b[i]))


base_values = {"A": 0, "C": 1, "G": 2, "T": 3}
terms = "ACGT"


def pattern_to_number(pattern):
    mers = pattern[::-1]
    v = base_values[mers[0]]
    for j in range(1, len(mers)):
        x = base_values[mers[j]] * 4 ** j
        v += x
    return v


def number_to_pattern(index, k):
    mers = ""
    while index:
        mers += terms[index % 4]
        index //= 4
    while len(mers) < k:
        mers += "A"
    return mers[::-1]


def d_neighborhood(pattern, d):
    k_mers = set()
    for indexes in combinations([i for i in range(len(pattern))], d):
        for chars in combinations_with_replacement(["A", "C", "G", "T"], d):
            arr = [b for b in pattern]
            for i, c in zip(indexes, chars):
                arr[i] = c
            k_mers.add(''.join(arr))
    return k_mers


def motif_enumeration(dna, k, d):
    k_mers = set()
    for pattern in dna:
        for i in range(len(pattern) - k + 1):
            k_mers.add(pattern[i:i + k])

    neighborhoods = set()
    for mer in k_mers:
        neighborhoods.update(d_neighborhood(mer, d))
    k_mers = list(neighborhoods)
    i = 0
    while i < len(k_mers):
        works = True
        for pattern in dna:
            if k_mers[i] in pattern:
                continue
            found = False
            for j in range(len(pattern) - k + 1):
                if hamming_distance(k_mers[i], pattern[j:j + k]) <= d:
                    found = True
                    break
            if not found:
                works = False
                break
        if not works:
            k_mers.pop(i)
        else:
            i += 1

    return set(k_mers)


def profile_matrix(patterns, pseudocounts=False):
    matrix = [[int(pseudocounts) for _ in range(len(patterns[0]))] for _ in range(4)]
    for pattern in patterns:
        for i in range(len(pattern)):
            matrix[base_values[pattern[i]]][i] += 1
    for i in range(len(matrix[0])):
        t = sum(matrix[j][i] for j in range(4))
        if t:
            for j in range(4):
                matrix[j][i] /= (t + int(pseudocounts) * 4)
    return matrix


def consensus(motifs):
    consensus_string = ""
    profile = profile_matrix(motifs)
    rot_profile = [[profile[j][i] for j in range(len(profile))] for i in range(len(motifs[0]))]
    for i in range(len(motifs[0])):
        x = [j for j in range(4) if rot_profile[i][j] == max(rot_profile[i])][0]
        consensus_string += terms[x]

    return consensus_string


def profile_most_probable(profile, pattern, k):
    most = 0
    most_i = 0
    for i in range(len(pattern) - k + 1):
        t = 1
        for j in range(k):
            t *= profile[base_values[pattern[i + j]]][j]
        if t > most:
            most = t
            most_i = i
    return pattern[most_i:most_i + k]


def greedy_motif_search(dna, k, t, pseudocounts=False):
    best_motifs = []
    best_motifs_score = 10**10

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            profile = profile_matrix(motifs, pseudocounts)
            motifs.append(profile_most_probable(profile, dna[j], k))
        consensus_string = consensus(motifs)
        score = sum(hamming_distance(motif, consensus_string) for motif in motifs)
        if score < best_motifs_score:
            best_motifs = motifs
            best_motifs_score = score
    return best_motifs


def minimum_distance(pattern, string):
    d = len(pattern) + 1
    for i in range(len(string) - len(pattern) + 1):
        hd = hamming_distance(pattern, string[i:i + len(pattern)])
        if hd < d:
            d = hd
            if hd == 0:
                return 0
    return d


def distance_between_pattern_and_strings(pattern, dna):
    return sum(map(lambda s: minimum_distance(pattern, s), dna))


def k_mer_composition(text, k, unique=False):
    k_mers = []
    for i in range(len(text) - k + 1):
        k_mers.append(text[i:i + k])
    if unique:
        return set(k_mers)
    return k_mers


def randomized_motif_search(dna, k, t):
    motifs = []
    for strand in dna:
        r = random.randint(0, len(strand) - k)
        motifs.append(strand[r:r + k])
    best_motifs = motifs
    best_consensus = consensus(best_motifs)
    best_score = sum(hamming_distance(motif, best_consensus) for motif in best_motifs)
    while True:
        profile = profile_matrix(motifs, pseudocounts=True)
        motifs = [profile_most_probable(profile, strand, k) for strand in dna]
        consensus_string = consensus(motifs)
        score = sum(hamming_distance(motif, consensus_string) for motif in motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
        else:
            return best_motifs, best_score


def gibbs_sampler(dna, k, t, n):
    best_motifs = []
    for strand in dna:
        r = random.randint(0, len(strand) - k)
        best_motifs.append(strand[r:r + k])
    best_consensus = consensus(best_motifs)
    best_score = sum(hamming_distance(motif, best_consensus) for motif in best_motifs)

    for j in range(n):
        i = random.randint(0, t)
        motifs = best_motifs
        profile = profile_matrix(motifs[:i] + motifs[i + 1:], pseudocounts=True)
        motifs[i] = profile

    return best_motifs, best_score
