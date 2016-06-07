#!/usr/bin/python

import cgitb,cgi,html,csvToDict
cgitb.enable()

print 'content-type: text/html\n'

qs = cgi.FieldStorage()

curr = csvToDict('accounts.csv')

if reguser in qs:
    reguser = qs['reguser'].value
    regpw = qs['regpw'].value
    re = qs['retype'].value
    if pw == re:
        dest = open('accounts.csv', 'a', 0)
        dest.write('\n' + user + ',' + pw)
        print html.h(1, 'SUCCESS! Now login on the main page.') #REDIRECT TO LOGIN PAGE
    else if pw != re:
        print html.h(1, 'The passwords do not match!') #IF POSSIBLE, REDIRECT TO REGISTER PAGE
    else if user in curr:
        print html.h(1, 'This username already exists.') #REDIRECTIONNNNNNN\
else:
    user = qs['user'].value
    pw = qs['pw'].value
    src = open('accounts.csv', 'rU')
    if user in curr and curr[user] == pw:
        #login success stuff
    else:
        print html.h(1, 'Incorrect username or password. Please try again.') #Redirect to homepage

#i am a super messy programmer whoops
