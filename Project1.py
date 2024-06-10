'''
Anastasia Makuyev
MATH 245 Project 1                                             Due 03/04/2022
Linear Algebra                                        Professor Barry Lederman
'''

def gcfAndDiophantine(x, y):
    a = x
    b = y
    c = 1
    d = 1
    if (b == a):
        return b, [b, 0]
    elif (b > a):                               #Switch a and b if b is greater than a         
        a, b = b, a
        
    listOfMultiples = []                        #This will be a list of the amount of times each "remainder" goes into the next number
    
    while (d > 0):                              #Let d be our iterator
        listOfMultiples.append(a // b)
        c = (a % b)                             #Let c be the remainder of a and b
        a = b
        b = c
        d = (a % b)

    listOfMultiples.reverse()
    
    listAdd = [0, 1]
    startingValue = 1
                
    for i in listAdd:
        if len(listAdd) <= (1 + len(listOfMultiples)):
            startingValue *= listOfMultiples[listAdd.index(i)]
            startingValue += i
            listAdd.append(startingValue)

    solutionSet = [listAdd[-2], listAdd[-1]]

    if (len(listOfMultiples) % 2) == 0:        #If there are an even number of values in the list:
        solutionSet[0] *= -1                   #Then the first value is negative.
    else:
        solutionSet[1] *= -1                   #Otherwise, the second value is negative.

    if (y > x):
        solutionSet.reverse()
        
    return c, solutionSet
    
print("Let's find the GCF and Diophantine solution of two integers.")
U = int(input("Enter the first integer: "))
V = int(input("Enter the second integer: "))
print ("The GCF of " + str(U) + " and " + str(V) + " is: " + str(gcfAndDiophantine(U,V)[0]))
print ("The ordered pair " + str((gcfAndDiophantine(U,V)[1])) +
       " is an integral solution of " +
       str(U) + "x + "+ str(V) + "y = " + str(gcfAndDiophantine(U,V)[0]))
