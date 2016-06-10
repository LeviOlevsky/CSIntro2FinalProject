#!/usr/bin/python

import cgitb,cgi,html,csvToDict,os,hashlib
cgitb.enable()

print 'content-type: text/html\n'

qs = cgi.FieldStorage()

curr = csvToDict.userToDict('accounts.csv')

temp = open('accounts.csv','rU').read().strip('\n')

if 'reguser' in qs:
    reguser = qs['reguser'].value
    regpw = qs['regpw'].value
    re = qs['retype'].value
    print html.headerWTags('Redirecting', '<meta http-equiv="refresh" content="2;url=tempindex.html"/>')
    if regpw == re and not reguser in curr:
        dest = open('accounts.csv', 'w', 0)
        dest.write(temp)
        dest.write('\n' + reguser + ',' + hashlib.sha256(regpw).hexdigest())
        dest.close()
        print html.heading(1, 'SUCCESS! Now login on the main page.')
        os.makedirs(reguser)#REDIRECT TO LOGIN PAGE
#MAKE NEW FILE
    elif reguser in curr:
        print html.heading(1, 'This username already exists.') #REDIRECTIONNNNNNN\
    elif regpw != re:
        print html.heading(1, 'The passwords do not match!') #IF POSSIBLE, REDIRECT TO REGISTER PAGE
else:
    user = qs['user'].value
    pw = qs['pw'].value
    if user in curr:
        if curr[user] == hashlib.sha256(pw).hexdigest():
            print html.headerWTags('Redirecting', '<meta http-equiv="refresh" content="2;url=' + user + '/TEMPLINK"/>')
            print html.heading(1, 'success')#login success stuff
        else:
            print html.headerWTags('Redirecting', '<meta http-equiv="refresh" content="2;url=tempindex.html"/>')
            print html.heading(1, 'Incorrect password. Please try again.') #Redirect to homepage
    else:
        print html.heading(1, 'Incorrect username. Please try again.') #Redirect to homepage

print html.heading(3, 'Redirecting in 2 seconds.')
#i am a super messy programmer whoops'''
