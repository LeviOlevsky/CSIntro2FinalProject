def csvToTermDict(file):
    source = open(file)
    contents = source.read()
    source.close()
    
    termsCommasList = contents.split('\n')
    # print termsCommasList
    '''['Levi,Olevsky', 'Helen,Ye', 
    'Elephant,Big Gray Animal', 'Zebra,Medium Gray Animal', 
    'Mouse,Small Gray Animal']'''
    dict = {}
    for element in termsCommasList:
            elementList = element.split(',')
            dict[elementList[0]] = elementList[1]
    return dict
    
# print csvToTermDict('terms.csv')
'''{'Levi': 'Olevsky', 'Elephant': 'Big Gray Animal', 
'Mouse': 'Small Gray Animal', 
'Zebra': 'Medium Gray Animal', 'Helen': 'Ye'}'''

def preserveOrder(file):
    source = open(file)
    contents = source.read()
    source.close()
    
    termsCommasList = contents.split('\n')
    # print termsCommasList
    '''['Levi,Olevsky', 'Helen,Ye', 
    'Elephant,Big Gray Animal', 'Zebra,Medium Gray Animal', 
    'Mouse,Small Gray Animal']'''
    list = []
    for element in termsCommasList:
            elementList = element.split(',')
            list.append(elementList[0])
    return list
    
# print preserveOrder('terms.csv')
'''['Levi', 'Helen', 'Elephant', 'Zebra', 'Mouse']'''