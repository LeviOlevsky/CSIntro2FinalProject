#!/usr/bin/python

import cgitb,cgi,html,csvToDict,os,hashlib,shutil
cgitb.enable()

print 'content-type: text/html\n'

qs = cgi.FieldStorage()

curr = csvToDict.userToDict('accounts.csv')

temp = open('accounts.csv','rU').read().strip('\n')

# This checks whether the person submitted a registratin or login form
if 'reguser' in qs:
    reguser = qs['reguser'].value
    regpw = qs['regpw'].value
    re = qs['retype'].value
    # This creates a header that redirects back to the homepage
    print html.headerWTags('Redirecting', '<meta http-equiv="refresh" content="2;url=index.html"/>')
    # This checks if the passwords match and if the username already exists
    # If so, add their information to the CSV and make a directory for their stuff
    if regpw == re and not reguser in curr:
        dest = open('accounts.csv', 'w', 0)
        dest.write(temp)
        dest.write('\n' + reguser + ',' + hashlib.sha256(regpw).hexdigest())
        dest.close()
        print html.heading(1, 'SUCCESS! Now login on the main page.')
        os.makedirs(reguser)
        shutil.copy2('homepage.py', reguser + '/homepage.py')
        shutil.copy2('quiz.html', reguser + '/quiz.html')
        shutil.copy2('flashCards.html', reguser + '/flashCards.html')
    elif reguser in curr:
        print html.heading(1, 'This username already exists.')
    elif regpw != re:
        print html.heading(1, 'The passwords do not match!')
# For when the person is trying to log in
else:
    user = qs['user'].value
    pw = qs['pw'].value
    # Makes sure the username exists and if not, prints redirection header
    if user in curr:
        # Checks if the encrypted password in CSV matches the encrypted one the user submitted
        # If so, successful login, if not, print redirection header
        if curr[user] == hashlib.sha256(pw).hexdigest():
            print html.headerWTags('Redirecting', '<meta http-equiv="refresh" content="2;url=' + user + '/homepage.py"/>')
            print html.heading(1, 'success')
            #login success stuff
        else:
            print html.headerWTags('Redirecting', '<meta http-equiv="refresh" content="2;url=index.html"/>')
            print html.heading(1, 'Incorrect password. Please try again.')
    else:
        print html.headerWTags('Redirecting', '<meta http-equiv="refresh" content="2;index.html"/>')
        print html.heading(1, 'Incorrect username. Please try again.')

print html.heading(3, 'Redirecting in 2 seconds.')
print html.footer()
