# Introduction to Random Strings
from math import log

s = "GATTTAAATGCGAGGTAGTGGCAAGTCCCAAGTTTTGTCTTACCTCGCGCGCGGGGGGAGGTGCCAACCGCGCCATGCCGTAAGGCA"
contents = [float(a) for a in "0.060 0.125 0.177 0.223 0.305 0.319 0.385 0.437 0.513 0.574 0.607 0.646 0.710 0.784 0.813 0.853 0.946".split()]

gc = len([a for a in s if a in ['C', 'G']])

probs = []

for c in contents:
    p = (c / 2) ** gc * ((1 - c) / 2) ** (len(s) - gc)
    probs.append(round(log(p, 10), 4))

print(' '.join([str(a) for a in probs]))