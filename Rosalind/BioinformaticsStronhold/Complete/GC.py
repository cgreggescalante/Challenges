# Identifying Unknown DNA Quickly

max_string = ""
max_value = 0

with open('rosalind_gc.txt', 'r') as file:
    lines = file.readlines()
    while len(lines) > 0:
        string = lines[0][:-1]
        i = 1
        dna = lines[1][:-1]
        lines = lines[2:]
        while len(lines) > 0 and not lines[0].startswith('>'):
            dna += lines[0][:-1]
            lines = lines[1:]

        counter = 0

        for a in dna:
            if a is 'C' or a is 'G':
                counter += 1

        percent = counter / len(dna) * 100

        if percent > max_value:
            max_value = percent
            max_string = string

    print(max_string)
    print(max_value)

