# Consensus and Profile
from Utils.FASTALoader import load

data = load('../Resources/rosalind_cons.txt')

profile = []

for i in range(len(data['Rosalind_2240'])):
    profile.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

    for key in data.keys():
        profile[i][data[key][i]] += 1

consensus = ""

for i in profile:
    m = 0
    c = ""
    for j in i.keys():
        if i[j] > m:
            m = i[j]
            c = j
    consensus += c

print(consensus)

for c in ['A', 'C', 'G', 'T']:
    print(c + ":", ' '.join([str(profile[i][c]) for i in range(len(profile))]))
