# Transcribing DNA into RNA

with open('../Resources/rosalind_rna.txt', 'r') as file:
    dna = file.readlines()[0][:-1]
    rna = ""

    for a in dna:
        if a == 'T':
            rna += 'U'
        else:
            rna += a

    print(rna)