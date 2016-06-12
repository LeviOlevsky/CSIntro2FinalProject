def header(title):
    return '''<!DOCTYPE html>
    <html>
    <head>
    <title>''' + title + '''</title>
    </head>
    <body>''' 

def headerWTags(title, tags):
    return '''<!DOCTYPE html>
    <html>
    <head>
    <title>''' + title + '</title>' + tags + '''</head>
    <body>''' 

def footer():
    return '''</body>
    </html>'''

def oneTable(list):
    inner = ''
    for item in list:
        inner += tableRow(tableData('<br>'+ '<center>' + item + '</center>' + '<br>' \
        '''<form action="csvToHtmlCardsDynamic.py">
         <input type="hidden" name="''' + item + '''" value="''' +  item + '''"> 
         <center><input type="submit" value="flip"></center>
        </form>''')) 
    return inner

def tableTop():
    return '''<table style="border-collapse:collapse;"border="1"><tbody>'''
  
def tableBttm():
    return '''</tbody></table>'''

def tableRow(item):
    return '<tr>' + str(item) + '</tr>'
    
def tableData(item):
    return '<td>' + str(item) + '</td>'

def tableHeader(item):
    return '<th>' + str(item) + '</th>'
    
def innerTable(dict):
    inner = ''
    for key in dict:
        inner += tableRow(tableData(key) + tableData(dict[key]['average']))
    return inner
 
def p(content):
    return '<p>' + str(content) + '</p>'

def heading(num, content):
    return '<h' + str(num) + '>' + content + '</h' + str(num) + '>'

def a(link, content):
    return '<a href="' + link + '">' + content + '</a>'
