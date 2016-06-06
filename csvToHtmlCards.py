#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n' 

import csvToDict
import html
import cgi

queryString = cgi.FieldStorage()

# leviTerms = csvToDict.csvToDict('leviTerms.csv')
# print leviTerms
'''{
'Levi': {'definition': 'Olevsky'}, 
'Elephant': {'definition': 'Big Gray Animal'}, 
'Mouse': {'definition': 'Small Gray Animal'}, 
'Zebra': {'definition': 'Medium Gray Animal'}, 
'Helen': {'definition': 'Ye'}
}'''

leviTerms = { 
            'Levi': 'Olevsky',
            'Elephant' : 'Big Gray Animal',
            'Mouse' : 'Small Gray Animal',
            'Zebra' : 'Medium Gray Animal',
            'Helen' : 'Ye'
            }
leviTermsList = leviTerms.keys()
#['Levi', 'Helen', 'Mouse', 'Zebra', 'Elephant']

def flipCard(list, dict, term):
    value = dict[term]
    list[list.index(term)] = value
    dict.pop(term)
    dict[value] = term

def flipCardWithTerm(term):
    flipCard(leviTermsList, leviTerms, term)
    
flipCardWithTerm('Levi') 


print '<center>' + html.header('cards'), \
      html.tableTop(), \
      html.oneTable(leviTermsList, leviTerms), \
      html.tableBttm(), \
      html.footer() + '</center>'
      
print queryString.value
