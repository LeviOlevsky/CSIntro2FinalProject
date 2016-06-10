#!/usr/bin/python

import cgitb,cgi,csvToDict,os.path
#cgitb.enable()

print 'content-type: text/html\n'

cards = csvToDict.userToDict('tempterms.csv')
terms = sorted(cards.keys())
defins = []
for key in terms:
    defins.append(cards[key])

qs = cgi.FieldStorage()
incorrect = []
if os.path.isfile('incorrect.csv'):
    aiDict = csvToDict.userToDict('incorrect.csv')
    for key in sorted(aiDict):
        incorrect.append(int(aiDict[key]))
else: 
    for i in range(len(qs)):
        incorrect.append(0)

def updateCorrect(ques, ans, terms, defins, incorrect):
    if not defins[terms.index(ques)] == ans:
        incorrect[terms.index(ques)] += 1
    return incorrect

def makeAIDict(incorrect, terms, defins, numTerms):
    ai = {}
    for i in range(numTerms):
        ind = incorrect.index(max(incorrect))
        incorrect.pop(ind)
        ai[terms.pop(ind)] = defins.pop(ind)
    return ai

for i in qs:
    updateCorrect(qs[i].name, qs[i].value, terms, defins, incorrect)

print incorrect

dest = open('incorrect.csv', 'w', 0)
i = 0
while i < len(incorrect):
    dest.write(terms[i] + ',' + str(incorrect[i]))
    if i < len(incorrect) - 1:
        dest.write('\n')
    i += 1
