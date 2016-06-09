#!/usr/bin/python

import cgitb,cgi,html,csvToDict
cgitb.enable()

print 'content-type: text/html\n'

qs = cgi.FieldStorage()

curr = csvToDict.userToDict('accounts.csv')

print html.headerWTags('Redirecting', '<meta http-equiv="refresh" content="2;url=tempindex.html"/>')

if 'reguser' in qs:
    reguser = qs['reguser'].value
    regpw = qs['regpw'].value
    re = qs['retype'].value
    if regpw == re and not reguser in curr:
        dest = open('accounts.csv', 'a', 0)
        dest.write(reguser + ',' + regpw)
        dest.close()
        print html.heading(1, 'SUCCESS! Now login on the main page.') #REDIRECT TO LOGIN PAGE
    elif reguser in curr:
        print html.heading(1, 'This username already exists.') #REDIRECTIONNNNNNN\
    elif regpw != re:
        print html.heading(1, 'The passwords do not match!') #IF POSSIBLE, REDIRECT TO REGISTER PAGE
else:
    user = qs['user'].value
    pw = qs['pw'].value
    if user in curr:
        if curr[user] == pw:
            print html.heading(1, 'success')#login success stuff
        else:
            print html.heading(1, 'Incorrect password. Please try again.') #Redirect to homepage
    else:
        print html.heading(1, 'Incorrect username. Please try again.') #Redirect to homepage

print html.heading(3, 'Redirecting in 2 seconds.')
#i am a super messy programmer whoops'''
