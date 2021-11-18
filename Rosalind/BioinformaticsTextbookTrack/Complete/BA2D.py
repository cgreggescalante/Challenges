# Implement GreedyMotifSearch
import os

from Rosalind.Misc import greedy_motif_search

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    k, t = map(int, lines[0].split())
    dna = [line.strip() for line in lines[1:t+1]]
    test_result = [line.strip() for line in lines[t+1:t+t+1]]


result = greedy_motif_search(dna, k, t)

if len(test_result):
    try:
        assert test_result == result
    except AssertionError:
        print(f"{result} should equal {test_result}")
else:
    print("\n".join(result))
