# Introduction to the Bioinformatics Armory
from Bio.Seq import Seq

with open("../Resources/rosalind_ini.txt", "r") as file:
    line = file.readline().strip()

    s = Seq(line)

    print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))
