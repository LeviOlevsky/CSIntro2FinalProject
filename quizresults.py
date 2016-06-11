#!/usr/bin/python

import cgitb,cgi,csvToDict,os.path
#cgitb.enable()

print 'content-type: text/html\n'

# Sorts terms and definitions
cards = csvToDict.userToDict('tempterms.csv')
terms = sorted(cards.keys())
defins = []
for key in terms:
    defins.append(cards[key])

# Checks if there is already a file storing the amount of incorrect answers
# If not, make a list of all zeros for the number of terms
qs = cgi.FieldStorage()
incorrect = []
if os.path.isfile('incorrect.csv'):
    aiDict = csvToDict.userToDict('incorrect.csv')
    for key in sorted(aiDict):
        incorrect.append(int(aiDict[key]))
else: 
    for i in range(len(qs)):
        incorrect.append(0)

# Adds one in the list for every question you get wrong
def updateCorrect(ques, ans, terms, defins, incorrect):
    if not defins[terms.index(ques)] == ans:
        incorrect[terms.index(ques)] += 1
    return incorrect

# Makes the dictionary associating the number of most incorrect terms specified
# With their definition
def makeAIDict(incorrect, terms, defins, numTerms):
    ai = {}
    for i in range(numTerms):
        ind = incorrect.index(max(incorrect))
        incorrect.pop(ind)
        ai[terms.pop(ind)] = defins.pop(ind)
    return ai

# Go through all the questions in the form and update the list of incorrect answers
for i in qs:
    updateCorrect(qs[i].name, qs[i].value, terms, defins, incorrect)

print incorrect

# Write the incorrect answers into a CSV file for storage
dest = open('incorrect.csv', 'w', 0)
i = 0
while i < len(incorrect):
    dest.write(terms[i] + ',' + str(incorrect[i]))
    if i < len(incorrect) - 1:
        dest.write('\n')
    i += 1
