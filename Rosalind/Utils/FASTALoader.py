from pip._vendor import requests


def load(file):
    if file.startswith('http://') or file.startswith('https://'):
        return remote_load(file)
    return local_load(file)


def remote_load(file):
    request = requests.get(file)
    data = []
    for l in request.iter_lines():
        data.append(l.decode('utf-8'))

    return ''.join(data[1:])


def local_load(file):
    document = {}
    with open(file, 'r') as data:
        lines = data.readlines()
        while len(lines) > 0:
            dna = ""
            string = lines[0][1:-1]
            lines = lines[1:]
            while len(lines) > 0 and not lines[0].startswith('>'):
                dna += lines[0]
                if dna[-1] == "\n":
                    dna = dna[:-1]
                lines = lines[1:]

            document[string] = dna

    return document
