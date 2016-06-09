#!/usr/bin/python

import cgitb,csvToDict,random,html
#cgitb.enable()

print 'content-type: text/html\n'

cards = csvToDict.userToDict('tempterms.csv')
terms = cards.keys()
defins = cards.values()
correct = range(len(cards))

def randomize(which, terms, defins):
    if which == 'terms':
        random.shuffle(terms)
        return terms
    else:
        random.shuffle(defins)
        return defins

def updateCorrect(_in, quesTerm, associated, correct):
    if associated[quesTerm.index(_in)] == _in:
        print 'nextquestion'
    else:
        correct[quesTerm.index(_in)] += 1
    return correct

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

print html.header('Quizzer')
print html.heading(2, 'Quiz yourself!')
print '<ol><form>'
for i in range(len(cards)):
    print '<li>' + randTerms[i]
    choices = fourChoices(defins)
    for j in range(4):
        print '<input type="radio" name="quiz' + str(i) + '" value="' + choices[j] + '">' + choices[j]
    print '</li>'
print '<input type="submit"></form></ol>'
print html.footer()
