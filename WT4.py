'''
Anastasia Makuyev
MATH 245 WT4                                                         Due 05/06/2022
Linear Algebra                                              Professor Barry Lederman
'''

import itertools

ourValues = list(itertools.permutations(['0', '120', '240', 'F1', 'F2', 'F3'], 3))
ourReturn = []
ourReturnCrossRef = []
ourWorkingList = []

for each in ourValues:
    ourWorkingList.append('( '+ each[0]+ ' x ' + each[1] + ' )')
    ourWorkingList.append(each[2])
    ourReturn.append(ourWorkingList)
    ourWorkingList = []

for each in ourValues:
    ourWorkingList.append(each[0])
    ourWorkingList.append('( '+ each[1]+ ' x ' + each[2] + ' )')
    ourReturnCrossRef.append(ourWorkingList)
    ourWorkingList = []

print(ourReturn)

out = ''
def calculateGroup(into):
    if into == '( 0 x 0 )':
        out = '0'
    elif into == '( 0 x 120 )':
        out = '120'
    elif into == '( 0 x 240 )':
        out = '240'
    elif into == '( 0 x F1 )':
        out = 'F1'
    elif into == '( 0 x F2 )':
        out = 'F2'
    elif into == '( 0 x F3 )':
        out = 'F3'
    elif into == '( 120 x 0 )':
        out = '120'
    elif into == '( 120 x 120 )':
        out = '240'
    elif into == '( 120 x 240 )':
        out = '0'
    elif into == '( 120 x F1 )':
        out = 'F2'
    elif into == '( 120 x F2 )':
        out = 'F3'
    elif into == '( 120 x F3 )':
        out = 'F1'
    elif into == '( 240 x 0 )':
        out = '240'
    elif into == '( 240 x 120 )':
        out = '0'
    elif into == '( 240 x 240 )':
        out = '120'
    elif into == '( 240 x F1 )':
        out = 'F3'
    elif into == '( 240 x F2 )':
        out = 'F1'
    elif into == '( 240 x F3 )':
        out = 'F2'
    elif into == '( F1 x 0 )':
        out = 'F1'
    elif into == '( F1 x 120 )':
        out = 'F3'
    elif into == '( F1 x 240 )':
        out = 'F2'
    elif into == '( F1 x F1 )':
        out = '0'
    elif into == '( F1 x F2 )':
        out = '240'
    elif into == '( F1 x F3 )':
        out = '120'
    elif into == '( F2 x 0 )':
        out = 'F2'
    elif into == '( F2 x 120 )':
        out = 'F1'
    elif into == '( F2 x 240 )':
        out = 'F3'
    elif into == '( F2 x F1 )':
        out = '120'
    elif into == '( F2 x F2 )':
        out = '0'
    elif into == '( F2 x F3 )':
        out = '240'
    elif into == '( F3 x 0 )':
        out = 'F3'
    elif into == '( F3 x 120 )':
        out = 'F2'
    elif into == '( F3 x 240 )':
        out = 'F1'
    elif into == '( F3 x F1 )':
        out = '240'
    elif into == '( F3 x F2 )':
        out = '120'
    elif into == '( F3 x F3 )':
        out = '0'
    return out

def finalCombiner1(firstGroup):
    answer = '( '+ calculateGroup(firstGroup[0])+ ' x ' + firstGroup[1] + ' )'
    return calculateGroup(answer)

def finalCombiner2(secondGroup):
    answer = '( '+ secondGroup[0]+ ' x ' + calculateGroup(secondGroup[1]) + ' )'
    return calculateGroup(answer)

for each in ourReturn:
    print('( '+ each[0]+ ' x ' + each[1] + ' )' + ' = ' + finalCombiner1(each))

print('---------------------------------------------------------------------------------------------------------------')

for each in ourReturnCrossRef:
    print('( '+ each[0]+ ' x ' + each[1] + ' )' + ' = ' + finalCombiner2(each))
    
 
