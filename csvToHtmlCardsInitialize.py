#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n'

import csvToDict
import html
import cgi
import csvToTermDict

queryString = cgi.FieldStorage()

# print queryDict
    
# print csvToTermDict('terms.csv')
'''{'Levi': 'Olevsky', 'Elephant': 'Big Gray Animal', 
'Mouse': 'Small Gray Animal', 
'Zebra': 'Medium Gray Animal', 'Helen': 'Ye'}'''
    
inputtedTerms = csvToTermDict.csvToTermDict('terms.csv')

def preFlipCard(dict, term):
    value = dict[term] #stores value of term you want to flip
    dict.pop(term) #pops out the term from the dict
    dict[value] = term #reverses the key and value pair in the dict

def flipCard(term): # simplifies the flipCard function
    preFlipCard(inputtedTerms, term)

def rewritePage():
    line1 = "inputtedTerms = csvToTermDict.csvToTermDict('terms.csv')"
    newLine1 = "inputtedTerms = " + str(inputtedTerms)
    source = open('csvToHtmlCardsDynamic.py', 'rU')
    contents = source.read()
    source.close()

    dest = open('csvToHtmlCardsDynamic.py', 'w', 0)
    dest.write(contents.replace(line1, newLine1))
    dest.close()

if len(queryString.keys()) != 0 and not(queryString.keys()[0] in inputtedTerms):
    flipCard(queryString.keys()[0])
    
print '<center>' + html.header('cards'), \
          html.tableTop(), \
          html.oneTable(inputtedTerms), \
          html.tableBttm(), \
          html.footer() + '</center>'

rewritePage()