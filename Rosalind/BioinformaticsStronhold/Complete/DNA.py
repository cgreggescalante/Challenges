# A Rapid Introduction to Molecular Biology

with open("../Resources/rosalind_dna.txt", 'r') as file:
    dna = file.readlines()[0][:-1]

    counter = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }

    for c in dna:
        counter[c] += 1

    print(counter['A'], counter['C'], counter['G'], counter['T'])
