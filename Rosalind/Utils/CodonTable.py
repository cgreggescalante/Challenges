codon_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
               'UUA': 'L',
               'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', 'UCU': 'S',
               'CCU': 'P',
               'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S', 'CCA': 'P',
               'ACA': 'T',
               'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N',
               'GAU': 'D',
               'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
               'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
               'UGC': 'C',
               'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W',
               'CGG': 'R',
               'AGG': 'R', 'GGG': 'G'}

r_codon_table = {'F': ['UUU', 'UUC'], 'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'], 'I': ['AUU', 'AUC', 'AUA'],
                 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'M': ['AUG'], 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                 'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'],
                 'A': ['GCU', 'GCC', 'GCA', 'GCG'],
                 'Y': ['UAU', 'UAC'], 'H': ['CAU', 'CAC'], 'N': ['AAU', 'AAC'], 'D': ['GAU', 'GAC'],
                 'Stop': ['UAA', 'UAG', 'UGA'], 'Q': ['CAA', 'CAG'], 'K': ['AAA', 'AAG'], 'E': ['GAA', 'GAG'],
                 'C': ['UGU', 'UGC'], 'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
                 'G': ['GGU', 'GGC', 'GGA', 'GGG'],
                 'W': ['UGG']}


def protein_from_rna(rna):
    return codon_table[rna]


def rna_from_protein(protein):
    return r_codon_table[protein]
