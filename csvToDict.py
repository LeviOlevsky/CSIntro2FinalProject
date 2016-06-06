
def getStringsOfLines( fileName):
    f = open( fileName, 'rU')
    oneString = f.read()
    f.close()
    listOfLines = oneString.split( '\n')
    return listOfLines

 
def csvToDict( fileName):
    dOL = {}
    stringsOfLines = getStringsOfLines(fileName)
    titles = stringsOfLines.pop(0).split(',')
    
    for line in stringsOfLines:
        fieldList = line.split(',')
        
        nonIdFields = {}

        curField = 1
        while curField < len( fieldList):
            nonIdFields[ titles[curField]] = fieldList[ curField]
            curField += 1
        
        
        dOL[ fieldList[0]] = nonIdFields
    return dOL

# print csvToDict( 'babe.csv')

def userToDict(_file):
    src = open(_file, 'rU')
    csvLines = []
    d = {}
    for line in src:
        csvLines.append(line.strip('\n').split(','))
    for i in range(len(csvLines)):
        d[csvLines[i][0]] = csvLines[i][1]
    return d

# print userToDict('accounts.csv')
