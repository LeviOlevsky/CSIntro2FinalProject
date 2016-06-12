#!/usr/bin/python

import cgitb,cgi,csvToDict,random,html
#cgitb.enable()

print 'content-type: text/html\n'

qs = cgi.FieldStorage()

# Randomizes, depending on which to randomize, the terms or definitions
def randomize(which, terms, defins):
    if which == 'terms':
        random.shuffle(terms)
        return terms
    else:
        random.shuffle(defins)
        return defins

# Make a dictionary from the terms from CSV and make appropriate lists for each
cards = csvToDict.cgiToDict()
terms = cards.keys()
defins = cards.values()
randTerms = randomize('terms', terms, defins)
# Make HTML page, which creates an ordered list with a multiple choice listing
# of all the terms/definitions and the associated one
print html.headerWTags('Quizzer', '<link rel="stylesheet" type="text/css" href="theme.css"')
print html.heading(2, 'Quiz yourself!')
print '<ol><form action="quizresults.py">'
for i in range(len(cards)):
    print '<li>' + randTerms[i] + '<br>'
    print '<input type="text" name="' + randTerms[i] + '">'
    print '</li>'
print '<input type="submit"></form></ol>'
print html.footer()
dest = open('../cards.csv', 'w', 0)
dest.write(qs['myFile'].value)
dest.close()
