# Mendel's First Law

k = 18
m = 20
n = 30

total = k + m + n

rec_rec = (n / total) * ((n - 1) / (total - 1))
het_het = (m / total) * ((m - 1) / (total - 1)) * .25
het_rec = (m / total) * (n / (total - 1)) * .5
rec_het = (n / total) * (m / (total - 1)) * .5

recessive = rec_rec + het_het + het_rec + rec_het

print(1 - recessive)
