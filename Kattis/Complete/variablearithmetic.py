# Variable Arithmetic

line = input()
variables = {}

while line != "0":
    if "=" in line:
        spl = line.split(" = ")
        variables[spl[0]] = int(spl[1])
    else:
        spl = line.split(" + ")
        for i in range(len(spl)):
            if spl[i] in variables:
                spl[i] = variables[spl[i]]
            try:
                val = int(spl[i])
                spl[i] = val
            except:
                pass
        spl = [str(sum([a for a in spl if type(a) == int]))] + [a for a in spl if type(a) == str]
        if spl[0] == '0':
            spl = spl[1:]
        print(' + '.join(spl))
    line = input()
