def userToDict(_file):
    src = open(_file, 'rU')
    csvLines = []
    d = {}
    for line in src:
        csvLines.append(line.strip('\n').split(','))
    for i in range(len(csvLines)):
        d[csvLines[i][0]] = csvLines[i][1]
    return d
