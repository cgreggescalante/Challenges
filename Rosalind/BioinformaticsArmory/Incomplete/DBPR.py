# Introduction to Protein Databases
from urllib import request

code = "Q5SLP9"
dat = request.urlopen(f"https://www.uniprot.org/uniprot/{code}.txt")

for l in dat.readlines():
    l = l.decode("utf-8").strip()[5:]
    if l.startswith("GO"):
        l = l[16:]
        if l.startswith("P"):
            print(l[2:].split(";")[0])
