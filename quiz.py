#!/usr/bin/python

import cgitb,csvToDict,random,html
#cgitb.enable()

print 'content-type: text/html\n'

# Make a dictionary from the terms from CSV and make appropriate lists for each
cards = csvToDict.userToDict('tempterms.csv')
terms = cards.keys()
defins = cards.values()

# Randomizes, depending on which to randomize, the terms or definitions
def randomize(which, terms, defins):
    if which == 'terms':
        random.shuffle(terms)
        return terms
    else:
        random.shuffle(defins)
        return defins

# Makes four choices out of the specified terms/definitions list
def fourChoices(defins):
    out = []
    out.append(random.choice(defins))
    while len(out) < 4:
        rand = random.choice(defins)
        if rand in out:
            pass
        else:
            out.append(rand)
    return out

randTerms = randomize('terms', terms, defins)

# Make HTML page, which creates an ordered list with a multiple choice listing
# of all the terms/definitions and the associated one
print html.header('Quizzer')
print html.heading(2, 'Quiz yourself!')
print '<ol><form action="quizresults.py">'
for i in range(len(cards)):
    print '<li>' + randTerms[i]
    choices = fourChoices(defins)
    if cards[randTerms[i]] not in choices:
        choices[random.randint(0,3)] = cards[randTerms[i]]
    for j in range(4):
        print '<input type="radio" name="' + randTerms[i] + '" value="' + choices[j] + '">' + choices[j]
    print '</li>'
print '<input type="submit"></form></ol>'
print html.footer()
