#!/usr/bin/python

import cgitb,cgi,html
cgitb.enable()

print 'content-type: text/html\n'

qs = cgi.FieldStorage()

dest = open('accounts.csv', 'a', 0)
user = qs['user'].value
pw = qs['pw'].value
re = qs['retype'].value
if pw == re:
    dest.write('\n' + user + ',' + pw)
    print html.h(1, 'SUCCESS! Now login on the main page.') #REDIRECT TO LOGIN PAGE
else:
    print html.h(1, 'The passwords do not match!') #IF POSSIBLE, REDIRECT TO REGISTER PAGE
