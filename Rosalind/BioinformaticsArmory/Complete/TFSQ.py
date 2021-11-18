# FASTQ format introduction
from Bio import SeqIO

records = SeqIO.index("../Resources/rosalind_tfsq.txt", "fastq")

for k in records:
    print(records[k].format("fasta"))

