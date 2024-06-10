'''
Anastasia Makuyev
MATH 245 WT2                                                         Due 02/25/2022
Linear Algebra                                              Professor Barry Lederman
'''

realNumbers = []                                    #Before we do anything, we must construct an array of all positive integers from 1 to 2000.

z = 1                                               #Using a counter variable,
while z <= 2000:                                    #And a while loop,
    realNumbers.append(z)                           #We can append all values from 1 to 2000 onto our null array.
    z+=1

workingArray = realNumbers.copy()
primeNumbers = []


workingArray.remove(1)                              #First, remove one from the list of numbers from 1 to 2000. It is the unit number.

n = 2                                               #n is a counter variable.


while n<2000:
    if (workingArray[0] in primeNumbers) == False:  #If the first value in our list of numbers from 1 to 2000 is not already in the list of prime numbers,
        primeNumbers.append(workingArray[0])        #Then we should add it to the list of prime numbers.


    for x in realNumbers:                           #Now, for every integer in our original and unchanging list of real numbers,
        if ((x%n)==0) and (x in workingArray):      #If that integer is divisible by our counter variable, and that integer is in the array of working numbers,
            workingArray.remove(x)                  #We should remove that number from our array of working numbers. We will no longer be working with it.
    n+=1                                            #Then n should iterate up by one, so our loop can keep going.
                                                    #B"H, may my code compile this time. 


print(primeNumbers)

