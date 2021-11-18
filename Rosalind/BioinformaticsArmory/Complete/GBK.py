# GenBank Introduction
from Bio import Entrez

Entrez.email = "conor@johngregg.org"

genus, start, stop = None, None, None

with open("../Resources/rosalind_gbk.txt", "r") as file:
    genus = file.readline().strip()
    start = file.readline().strip()
    stop = file.readline().strip()

handle = Entrez.esearch(db="nucleotide", term=f'(({genus}[Organism]) AND ("{start}"[Publication Date] : "{stop}"[Publication Date]))')
record = Entrez.read(handle)
print(record["Count"])
