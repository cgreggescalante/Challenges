# Data Formats
from Bio import Entrez

Entrez.email = "conor@johngregg.org"
ids = None

with open("../Resources/rosalind_frmt.txt", "r") as file:
    ids = file.readline().split()

handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
records = [r.strip() for r in handle.read().split(">") if len(r)]

records = sorted(records, key=lambda x: len(x[x.find("\n"):]))

print(f">{records[0]}")
