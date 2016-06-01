#! /usr/bin/python

import cgitb
cgitb.enable()

print 'content-type: text/html\n' 

import csvToDict

leviTerms = csvToDict.csvToDict('leviTerms.csv')
# print leviTerms
'''{
'Levi': {'definition': 'Olevsky'}, 
'Elephant': {'definition': 'Big Gray Animal'}, 
'Mouse': {'definition': 'Small Gray Animal'}, 
'Zebra': {'definition': 'Medium Gray Animal'}, 
'Helen': {'definition': 'Ye'}
}'''

