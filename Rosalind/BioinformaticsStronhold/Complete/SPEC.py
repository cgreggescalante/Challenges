# Inferring Protein From Spectrum

masses = []

with open("../../Utils/monoisotopicMassTable", 'r') as file:
    lines = file.readlines()

    for line in lines:
        ls = line.split()
        masses.append([ls[0], float(ls[1])])

proteins = ""

with open("../Resources/rosalind_spec.txt", 'r') as file:
    lines = file.readlines()

    prev = float(lines[0][:-1])
    for line in lines:
        l = float(line[:-1])
        m = l - prev
        for a in masses:
            if abs(a[1] - m) < .001:
                proteins += a[0]
                break
        prev = l

print(proteins)
