# Overlap Graphs
from Utils.FASTALoader import load

data = load("../Resources/rosalind_grph.txt")

keys = [k for k in data.keys()]

for i in range(len(keys)):
    suff = data[keys[i]][-3:]

    for j in range(len(keys)):
        if data[keys[j]][:3] == suff and data[keys[i]] != data[keys[j]]:
            print(keys[i], keys[j])
